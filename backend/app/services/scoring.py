import re
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.progress import ModuleProgress
from app.models.user import User


def normalize(value: str) -> str:
    text = value.strip().lower()
    text = text.replace("\u2019", "'").replace("`", "'")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[.!?]+$", "", text)
    return text


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
) -> bool:
    candidates = [answer, *(accepted or [])]
    given_n = normalize(given)
    norm_cands = [normalize(item) for item in candidates]
    if any(given_n == item for item in norm_cands):
        return True

    if prompt and "___" in prompt:
        for cand in candidates:
            cand_n = normalize(cand)
            filled_cand = normalize(prompt.replace("___", cand, 1))
            filled_given = normalize(prompt.replace("___", given, 1))
            if filled_given == filled_cand:
                return True
            blank = _infer_blank(prompt, cand)
            if blank and given_n == normalize(blank):
                return True
            if " " not in cand_n and " " in given_n:
                inferred = _infer_blank(prompt, given)
                if inferred is not None and normalize(inferred) == cand_n:
                    return True
            if blank is None and "___" not in cand:
                inferred_from_given = _infer_blank(prompt, given)
                inferred_from_cand = _infer_blank(prompt, cand)
                if (
                    inferred_from_given
                    and inferred_from_cand
                    and normalize(inferred_from_given) == normalize(inferred_from_cand)
                ):
                    return True
        return False

    for cand_n in norm_cands:
        if " " not in cand_n and len(cand_n) <= 24 and cand_n in given_n.split() and len(given_n.split()) <= 8:
            if given_n == cand_n or given_n.endswith(cand_n) or given_n.startswith(cand_n):
                return True
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
