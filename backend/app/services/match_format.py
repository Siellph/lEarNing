"""Match exercise helpers: parse a=b;c=d, expose left/right sides, score pairs."""

from __future__ import annotations

import re
from collections import Counter

_SPACEY = re.compile(r"[\s+/→\-]+")


def _cmp(value: str) -> str:
    text = (value or "").strip().lower().replace("\u2019", "'").replace("`", "'")
    text = re.sub(r"\s+", " ", text)
    return text


def parse_pairs(answer: str) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for part in (answer or "").split(";"):
        part = part.strip()
        if not part or "=" not in part:
            continue
        left, right = part.split("=", 1)
        left, right = left.strip(), right.strip()
        if left and right:
            pairs.append((left, right))
    return pairs


def format_pairs(pairs: list[tuple[str, str]]) -> str:
    return "; ".join(f"{left}={right}" for left, right in pairs)


def _norm_key(value: str) -> str:
    return _SPACEY.sub("", (value or "").strip().lower())


def _best_option(key: str, options: list[str], used: set[str]) -> str | None:
    if key in options and key not in used:
        return key
    kn = _norm_key(key)
    ranked: list[tuple[int, str]] = []
    for opt in options:
        if opt in used:
            continue
        if opt == key:
            return opt
        on = _norm_key(opt)
        if kn == on:
            ranked.append((0, opt))
        elif kn and on and (kn in on or on in kn):
            ranked.append((1 + abs(len(on) - len(kn)), opt))
        elif key in opt or opt in key:
            ranked.append((2 + abs(len(opt) - len(key)), opt))
    if not ranked:
        return None
    ranked.sort(key=lambda item: item[0])
    return ranked[0][1]


def align_answer(left_options: list[str], answer: str) -> str:
    """Rewrite pair left keys to match option strings when seeds used shortened keys."""
    pairs = parse_pairs(answer)
    if not pairs:
        return (answer or "").strip()
    used: set[str] = set()
    aligned: list[tuple[str, str]] = []
    for key, right in pairs:
        opt = _best_option(key, left_options, used) if left_options else key
        if opt is None:
            opt = key
        used.add(opt)
        aligned.append((opt, right))
    return format_pairs(aligned)


def rights_from_pairs(pairs: list[tuple[str, str]]) -> list[str]:
    """Right-side chips for UI — keep duplicates when several slots share a label."""
    return [right for _, right in pairs]


def unique_rights(pairs: list[tuple[str, str]]) -> list[str]:
    """Backward-compatible alias; duplicates are preserved (needed for equal slot/chip counts)."""
    return rights_from_pairs(pairs)


def ensure_right_multiset(existing: list[str], needed: list[str]) -> list[str]:
    """Keep distractors, but guarantee at least the multiset of answer rights."""
    have = Counter(existing)
    need = Counter(needed)
    out = list(existing)
    for label, count in need.items():
        for _ in range(max(0, count - have[label])):
            out.append(label)
    return out


def sides_from_payload(options, answer: str | None = None) -> dict[str, list[str]]:
    """Return {left, right} for UI. Accepts legacy list options or {left,right} dict."""
    left: list[str] = []
    right: list[str] = []
    if isinstance(options, dict):
        left = [str(x) for x in (options.get("left") or []) if str(x).strip()]
        right = [str(x) for x in (options.get("right") or []) if str(x).strip()]
    elif isinstance(options, list):
        left = [str(x) for x in options if str(x).strip()]

    pairs = parse_pairs(answer or "")
    if not left and pairs:
        left = [a for a, _ in pairs]
    needed = rights_from_pairs(pairs)
    if needed:
        right = ensure_right_multiset(right, needed) if right else needed
    return {"left": left, "right": right}


def normalize_match_payload(options, answer: str | None = None) -> tuple[dict[str, list[str]], str]:
    """Build {left,right} + aligned answer from legacy list options / free-form answers."""
    opts: list[str] = []
    existing_right: list[str] = []
    if isinstance(options, dict):
        opts = [str(x).strip() for x in (options.get("left") or []) if str(x).strip()]
        existing_right = [str(x).strip() for x in (options.get("right") or []) if str(x).strip()]
        if opts and existing_right and looks_like_match_answer(answer or ""):
            aligned = align_answer(opts, answer or "")
            needed = rights_from_pairs(parse_pairs(aligned))
            return {"left": opts, "right": ensure_right_multiset(existing_right, needed)}, aligned
        if opts and existing_right and not (answer or "").strip():
            # Prefer zip only when counts already match; otherwise leave as-is for repair.
            if len(opts) == len(existing_right):
                return {"left": opts, "right": existing_right}, format_pairs(list(zip(opts, existing_right)))
            return {"left": opts, "right": existing_right}, ""
    elif isinstance(options, list):
        opts = [str(x).strip() for x in options if str(x).strip()]

    ans = (answer or "").strip()

    # Arrow-encoded option strings are unambiguous pair encodings (unlike bare '=').
    if opts and all(("→" in o or "->" in o) for o in opts) and not looks_like_match_answer(ans):
        pairs = []
        for o in opts:
            sep = "→" if "→" in o else "->"
            left, right = o.split(sep, 1)
            pairs.append((left.strip(), right.strip()))
        return {"left": [a for a, _ in pairs], "right": rights_from_pairs(pairs)}, format_pairs(pairs)

    # Bare '=' in options only when answer is empty (labels like "avoid=-ing" are slots).
    if opts and not ans and all("=" in o for o in opts):
        pairs = []
        for o in opts:
            left, right = o.split("=", 1)
            pairs.append((left.strip(), right.strip()))
        return {"left": [a for a, _ in pairs], "right": rights_from_pairs(pairs)}, format_pairs(pairs)

    if looks_like_match_answer(ans) or (ans.count("=") >= 1 and parse_pairs(ans)):
        aligned = align_answer(opts, ans)
        needed = rights_from_pairs(parse_pairs(aligned))
        left = opts if opts else [a for a, _ in parse_pairs(aligned)]
        right = ensure_right_multiset(existing_right, needed) if existing_right else needed
        return {"left": left, "right": right}, aligned

    rights = [p.strip() for p in re.split(r"\s*;\s*", ans) if p.strip()]
    if len(rights) == len(opts) and opts:
        pairs = list(zip(opts, rights))
        return {"left": opts, "right": rights_from_pairs(pairs)}, format_pairs(pairs)

    loose = [p.strip() for p in re.split(r"\s*[;/|]\s*", ans) if p.strip()]
    if len(loose) == len(opts) and opts:
        pairs = list(zip(opts, loose))
        return {"left": opts, "right": rights_from_pairs(pairs)}, format_pairs(pairs)

    sides = sides_from_payload(
        {"left": opts, "right": existing_right} if (opts or existing_right) else opts,
        ans,
    )
    return sides, ans if ans else format_pairs([])


def public_match_options(options, answer: str | None = None) -> dict[str, list[str]] | None:
    sides, _ = normalize_match_payload(options, answer)
    if not sides["left"] or not sides["right"]:
        return None
    return sides


def looks_like_match_answer(answer: str | None) -> bool:
    if not answer or "=" not in answer:
        return False
    return len(parse_pairs(answer)) >= 2


def pair_set(answer: str) -> frozenset[tuple[str, str]]:
    return frozenset((_cmp(left), _cmp(right)) for left, right in parse_pairs(answer))


def is_match_correct(given: str, answer: str) -> bool:
    """Order-independent pair compare; tolerates shortened left keys in expected answer."""
    given_pairs = parse_pairs(given)
    answer_pairs = parse_pairs(answer)
    if not given_pairs or not answer_pairs or len(given_pairs) != len(answer_pairs):
        return False

    if pair_set(given) == pair_set(answer):
        return True

    remaining = list(answer_pairs)
    for g_left, g_right in given_pairs:
        g_ln, g_rn = _cmp(g_left), _cmp(g_right)
        hit = -1
        for i, (a_left, a_right) in enumerate(remaining):
            a_ln, a_rn = _cmp(a_left), _cmp(a_right)
            left_ok = g_ln == a_ln or a_ln in g_ln or g_ln in a_ln or _norm_key(g_left) == _norm_key(a_left)
            if left_ok and g_rn == a_rn:
                hit = i
                break
        if hit < 0:
            return False
        remaining.pop(hit)
    return not remaining


def match_payload_ok(options, answer: str | None = None) -> bool:
    """True when every left slot can be filled (rights cover answer multiset)."""
    sides, aligned = normalize_match_payload(options, answer)
    left = sides.get("left") or []
    right = sides.get("right") or []
    pairs = parse_pairs(aligned)
    if not left or not right:
        return False
    if pairs and len(pairs) != len(left):
        return False
    needed = Counter(rights_from_pairs(pairs)) if pairs else Counter()
    have = Counter(right)
    if needed and any(have[label] < n for label, n in needed.items()):
        return False
    # Soft-lock: fewer chips than slots with no distractor strategy
    if len(right) < len(left):
        return False
    return True
