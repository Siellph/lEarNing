import re
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.progress import ModuleProgress
from app.models.user import User

# Bidirectional via expand→full form: don't ↔ do not, I'm ↔ I am, can't ↔ cannot, …
_CONTRACTION_EXPAND: list[tuple[re.Pattern[str], str]] = [
    (re.compile(rf"\b{re.escape(short)}\b", re.I), full)
    for short, full in [
        ("i'm", "i am"),
        ("i've", "i have"),
        ("i'd", "i would"),
        ("i'll", "i will"),
        ("you're", "you are"),
        ("you've", "you have"),
        ("you'd", "you would"),
        ("you'll", "you will"),
        ("he's", "he is"),
        ("she's", "she is"),
        ("it's", "it is"),
        ("we're", "we are"),
        ("we've", "we have"),
        ("we'd", "we would"),
        ("we'll", "we will"),
        ("they're", "they are"),
        ("they've", "they have"),
        ("they'd", "they would"),
        ("they'll", "they will"),
        ("isn't", "is not"),
        ("aren't", "are not"),
        ("wasn't", "was not"),
        ("weren't", "were not"),
        ("don't", "do not"),
        ("doesn't", "does not"),
        ("didn't", "did not"),
        ("can't", "cannot"),
        ("won't", "will not"),
        ("shouldn't", "should not"),
        ("wouldn't", "would not"),
        ("couldn't", "could not"),
        ("mustn't", "must not"),
        ("needn't", "need not"),
        ("haven't", "have not"),
        ("hasn't", "has not"),
        ("hadn't", "had not"),
        ("let's", "let us"),
        ("that's", "that is"),
        ("what's", "what is"),
        ("where's", "where is"),
        ("who's", "who is"),
        ("there's", "there is"),
        ("here's", "here is"),
    ]
]
# Longer n't-forms first is unnecessary (each pattern is whole-word); apply "can not" → cannot.
_CAN_NOT = re.compile(r"\bcan not\b", re.I)


def normalize(value: str) -> str:
    """Casefold, ё→е, unify apostrophes, collapse spaces, strip trailing .!? — no contraction expand."""
    text = value.strip().casefold()
    text = text.replace("ё", "е")
    text = text.replace("\u2019", "'").replace("`", "'")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[.!?]+$", "", text)
    return text


# Gloss alternatives in vocab translations: «стакан; стекло», «glass / cup», …
_ANSWER_ALT_SPLIT = re.compile(r"\s*[;/、,]\s*")


def split_answer_alternatives(value: str) -> list[str]:
    """Split a stored gloss into OR-alternatives; single values return as a one-item list."""
    text = value.strip()
    if not text:
        return []
    parts = [part.strip() for part in _ANSWER_ALT_SPLIT.split(text) if part.strip()]
    return parts or [text]


def expand_contractions(text: str) -> str:
    """Map contracted forms to full forms so don't and do not compare equal."""
    out = text
    for pattern, full in _CONTRACTION_EXPAND:
        out = pattern.sub(full, out)
    out = _CAN_NOT.sub("cannot", out)
    return re.sub(r"\s+", " ", out).strip()


def for_compare(value: str) -> str:
    """Canonical key for answer matching (normalize + expand contractions).

    Gap separators `` / `` and ``,`` collapse to spaces so ``have / had`` ≡ ``have had``.
    """
    text = expand_contractions(normalize(value))
    text = re.sub(r"\s*[/,]\s*", " ", text)
    return re.sub(r"\s+", " ", text).strip()


_MARKER_IN_PROMPT = re.compile(r"[«\"]([^»\"]{2,40})[»\"]")


def missing_required_marker_hint(given: str, answer: str, prompt: str | None) -> str | None:
    """If the core clause matches but a quoted time/marker from the prompt is missing."""
    if not prompt or not answer or not given:
        return None
    markers = _MARKER_IN_PROMPT.findall(prompt)
    if not markers:
        return None
    given_n = for_compare(given)
    answer_n = for_compare(answer)
    if given_n == answer_n:
        return None
    missing = []
    for marker in markers:
        marker_n = for_compare(marker)
        if marker_n in answer_n and marker_n not in given_n:
            missing.append(marker)
    if not missing:
        return None
    core = answer_n
    for marker in missing:
        core = core.replace(for_compare(marker), " ")
    core = re.sub(r"\s+", " ", core).strip()
    if not core or (given_n != core and given_n not in answer_n and answer_n.find(given_n) == -1):
        return None
    joined = ", ".join(f"«{m}»" for m in missing)
    return f"Почти верно по времени/форме — добавьте в ответ маркер {joined}."


def _infer_blank(prompt: str, completed: str) -> str | None:
    """If prompt has ___ and completed is the filled phrase, return the blank value."""
    if "___" not in prompt:
        return None
    left, right = prompt.split("___", 1)
    left_toks = [normalize(t) for t in re.findall(r"[A-Za-z']+", left)]
    right_toks = [normalize(t) for t in re.findall(r"[A-Za-z']+", right)]
    comp_toks = normalize(completed).split()
    if not comp_toks:
        return None
    prefix = left_toks[-3:] if left_toks else []
    suffix = right_toks[:3] if right_toks else []
    for i in range(len(comp_toks) + 1):
        if prefix and comp_toks[i : i + len(prefix)] != prefix:
            continue
        start = i + len(prefix)
        if not suffix:
            middle = " ".join(comp_toks[start:])
            return middle or None
        for j in range(start, len(comp_toks) + 1):
            if comp_toks[j : j + len(suffix)] == suffix:
                return " ".join(comp_toks[start:j]) or None
        if prefix:
            break
    return None


def is_correct(
    given: str,
    answer: str,
    accepted: list[str] | None = None,
    prompt: str | None = None,
    kind: str | None = None,
) -> bool:
    from app.services.match_format import is_match_correct, looks_like_match_answer

    if kind == "match" or looks_like_match_answer(answer):
        if is_match_correct(given, answer):
            return True
        for alt in accepted or []:
            if is_match_correct(given, alt):
                return True
        return False

    candidates = [answer, *(accepted or [])]
    given_n = for_compare(given)
    norm_cands = [for_compare(item) for item in candidates]
    if any(given_n == item for item in norm_cands):
        return True

    if prompt and "___" in prompt:
        for cand in candidates:
            cand_n = for_compare(cand)
            filled_cand = for_compare(prompt.replace("___", cand, 1))
            filled_given = for_compare(prompt.replace("___", given, 1))
            if filled_given == filled_cand:
                return True
            blank = _infer_blank(prompt, cand)
            if blank and given_n == for_compare(blank):
                return True
            if " " not in cand_n and " " in given_n:
                inferred = _infer_blank(prompt, given)
                if inferred is not None and for_compare(inferred) == cand_n:
                    return True
            if blank is None and "___" not in cand:
                inferred_from_given = _infer_blank(prompt, given)
                inferred_from_cand = _infer_blank(prompt, cand)
                if (
                    inferred_from_given
                    and inferred_from_cand
                    and for_compare(inferred_from_given) == for_compare(inferred_from_cand)
                ):
                    return True
        return False

    for cand_n in norm_cands:
        if " " not in cand_n and len(cand_n) <= 24 and cand_n in given_n.split() and len(given_n.split()) <= 8:
            if given_n == cand_n or given_n.endswith(cand_n) or given_n.startswith(cand_n):
                return True
    return False


def vocab_is_correct(given: str, expected: str) -> bool:
    """Vocab check: accept any one alternative; full multi-gloss string still matches."""
    alts = split_answer_alternatives(expected)
    if is_correct(given, expected, alts):
        return True
    given_parts = split_answer_alternatives(given)
    if len(given_parts) > 1:
        return all(any(is_correct(part, alt) for alt in alts) for part in given_parts)
    return False


def percent(correct: int, total: int) -> int:
    if total <= 0:
        return 0
    return round(correct * 100 / total)


def touch_user(db: Session, user: User, xp: int = 0) -> None:
    now = datetime.now(timezone.utc)
    if user.last_activity:
        last = user.last_activity
        if last.tzinfo is None:
            last = last.replace(tzinfo=timezone.utc)
        delta = now.date() - last.date()
        if delta.days == 1:
            user.streak += 1
        elif delta.days > 1:
            user.streak = 1
    else:
        user.streak = max(user.streak, 1)
    user.last_activity = now
    user.xp += xp
    db.add(user)


def get_or_create_progress(db: Session, user_id: int, module_id: int) -> ModuleProgress:
    progress = (
        db.query(ModuleProgress)
        .filter(ModuleProgress.user_id == user_id, ModuleProgress.module_id == module_id)
        .first()
    )
    if not progress:
        progress = ModuleProgress(user_id=user_id, module_id=module_id, status="in_progress")
        db.add(progress)
        db.flush()
    return progress


def refresh_module_status(progress: ModuleProgress) -> None:
    if progress.test_score is not None and progress.test_score >= 70:
        progress.status = "completed"
    elif progress.lesson_done or progress.practice_score > 0:
        progress.status = "in_progress"
    else:
        progress.status = "not_started"
