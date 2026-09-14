"""Study decks API: irregular verbs, idioms, exceptions (vocab-like batches)."""

import math
import random
from collections import defaultdict
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.study import StudyCard, StudyDeck, StudyProgress
from app.models.user import User
from app.schemas.content import StudyCheckIn
from app.services.scoring import is_correct, touch_user

router = APIRouter(prefix="/study", tags=["study"])

BATCH_SIZE = 10
KINDS = {"verbs", "idioms", "exceptions"}
STRENGTH_TARGET = 5

# Mastery bits — track which required facets are done in the current pass.
# Idioms/exceptions: leave the queue when strength >= STRENGTH_TARGET (bits reset
# conceptually via a new full pass when both directions are already done).
# Verbs: leave when all required facets are correct once — strength is display-only.
MASTERY_BITS = {
    "choice_en_ru": 1,
    "choice_ru_en": 2,
    "choice_v2": 4,
    "choice_v3": 8,
    "choice_forms": 12,  # both form bits when combined task is used
    "type_v2": 4,
    "type_v3": 8,
    # Legacy aliases from free-text / one-way packs.
    "choice_translation": 1,
    "type_translation": 1,
}
# Idioms / exceptions: both meaning (or rule↔form) sides.
MEANING_MASTERY = 3
# Verbs: EN↔RU + V2 + V3.
VERB_LEARNED_MASTERY = 15
TASK_KINDS_DEFAULT = ("choice_en_ru", "choice_ru_en")
TASK_KINDS_VERBS = ("choice_en_ru", "choice_ru_en", "choice_v2", "choice_v3")


def _cards(db: Session, deck: StudyDeck) -> list[StudyCard]:
    return db.query(StudyCard).filter(StudyCard.deck_id == deck.id).order_by(StudyCard.sort_order, StudyCard.id).all()


def _progress_maps(db: Session, user_id: int, card_ids: list[int]) -> tuple[dict[int, int], dict[int, int]]:
    if not card_ids:
        return {}, {}
    rows = (
        db.query(StudyProgress)
        .filter(StudyProgress.user_id == user_id, StudyProgress.card_id.in_(card_ids))
        .all()
    )
    strength = {row.card_id: row.strength for row in rows}
    mastery = {row.card_id: int(getattr(row, "mastery", 0) or 0) for row in rows}
    return strength, mastery


def _batch_count(total: int) -> int:
    return max(1, math.ceil(total / BATCH_SIZE)) if total else 1


def _learned_mask(deck_kind: str) -> int:
    return VERB_LEARNED_MASTERY if deck_kind == "verbs" else MEANING_MASTERY


def _is_learned(strength: int, mastery: int = 0, deck_kind: str = "") -> bool:
    """Verbs: all required facets once. Idioms/exceptions: strength target."""
    if deck_kind == "verbs":
        return (mastery & VERB_LEARNED_MASTERY) == VERB_LEARNED_MASTERY
    return strength >= STRENGTH_TARGET


def _pass_complete(mastery_value: int, deck_kind: str = "") -> bool:
    mask = _learned_mask(deck_kind) if deck_kind == "verbs" else MEANING_MASTERY
    return (mastery_value & mask) == mask


def _mastery_count(mastery_value: int, deck_kind: str = "") -> int:
    mask = _learned_mask(deck_kind)
    return bin(mastery_value & mask).count("1")


def _mastery_total(deck_kind: str) -> int:
    return 4 if deck_kind == "verbs" else 2


def _suggested_batch(
    cards: list[StudyCard],
    strength: dict[int, int],
    mastery: dict[int, int],
    deck_kind: str,
) -> int:
    n = _batch_count(len(cards))
    for index in range(n):
        chunk = cards[index * BATCH_SIZE : (index + 1) * BATCH_SIZE]
        if any(
            not _is_learned(strength.get(card.id, 0), mastery.get(card.id, 0), deck_kind)
            for card in chunk
        ):
            return index + 1
    return n


def _card_out(card: StudyCard, strength: int = 0, mastery_value: int = 0, deck_kind: str = "") -> dict:
    return {
        "id": card.id,
        "primary_text": card.primary_text,
        "secondary_text": card.secondary_text,
        "tertiary_text": card.tertiary_text,
        "translation": card.translation,
        "example": card.example,
        "example_translation": card.example_translation,
        "category": card.category,
        "strength": strength,
        "mastery": mastery_value,
        "mastery_count": _mastery_count(mastery_value, deck_kind),
        "mastery_total": _mastery_total(deck_kind),
        "learned": _is_learned(strength, mastery_value, deck_kind),
    }


def _options(correct: str, pool: list[StudyCard], attr: str, extra: list[StudyCard] | None = None, n: int = 3) -> list[str]:
    seen = {correct.strip().lower()}
    distractors: list[str] = []
    for source in (pool, extra or []):
        for card in source:
            value = getattr(card, attr) or ""
            key = value.strip().lower()
            if not key or key in seen:
                continue
            seen.add(key)
            distractors.append(value)
    random.shuffle(distractors)
    choices = [correct, *distractors[:n]]
    random.shuffle(choices)
    return choices[: n + 1]


def _form_pair(card: StudyCard) -> str:
    v2 = (card.secondary_text or "").strip()
    v3 = (card.tertiary_text or "").strip()
    if v2 and v3:
        return f"{v2} · {v3}"
    return v2 or v3


def _form_pair_options(correct: str, pool: list[StudyCard], extra: list[StudyCard] | None = None, n: int = 3) -> list[str]:
    seen = {correct.strip().lower()}
    distractors: list[str] = []
    for source in (pool, extra or []):
        for card in source:
            value = _form_pair(card)
            key = value.strip().lower()
            if not key or key in seen:
                continue
            seen.add(key)
            distractors.append(value)
    random.shuffle(distractors)
    choices = [correct, *distractors[:n]]
    random.shuffle(choices)
    return choices[: n + 1]


def _verb_forms_speak(card: StudyCard) -> str:
    """Plain TTS for irregular verbs: V1, V2, V3 with pauses; expand slash alts; no gloss."""
    parts: list[str] = []
    for field in (
        card.primary_text.split("→")[0].strip(),
        (card.secondary_text or "").strip(),
        (card.tertiary_text or "").strip(),
    ):
        if not field:
            continue
        parts.extend(p.strip() for p in field.split("/") if p.strip())
    return ". ".join(parts)


def _card_speak(card: StudyCard, deck_kind: str) -> str:
    if deck_kind == "verbs":
        return _verb_forms_speak(card)
    return card.primary_text.split("→")[0].strip()


def _task_kinds_for(deck_kind: str) -> tuple[str, ...]:
    if deck_kind == "verbs":
        return TASK_KINDS_VERBS
    return TASK_KINDS_DEFAULT


def _build_task(
    card: StudyCard,
    kind: str,
    pool: list[StudyCard],
    deck_cards: list[StudyCard],
    deck_kind: str,
) -> dict:
    # Exceptions: front = pattern/form, back = rule (RU) — not a translation pair.
    if deck_kind == "exceptions":
        if kind == "choice_en_ru":
            return {
                "uid": f"enru-{card.id}",
                "id": card.id,
                "kind": kind,
                "prompt": f"Какое правило верно для «{card.primary_text}»?",
                "options": _options(card.translation, pool, "translation", deck_cards),
                "speak": _card_speak(card, deck_kind),
                "target": "translation",
                "example": card.example or None,
            }
        return {
            "uid": f"ruen-{card.id}",
            "id": card.id,
            "kind": kind,
            "prompt": f"К какой форме относится правило: «{card.translation}»?",
            "options": _options(card.primary_text, pool, "primary_text", deck_cards),
            "target": "primary",
            "example": card.example or None,
        }

    if deck_kind == "verbs":
        v1 = card.primary_text
        v2 = card.secondary_text or ""
        v3 = card.tertiary_text or ""
        if kind == "choice_v2":
            return {
                "uid": f"v2-{card.id}",
                "id": card.id,
                "kind": kind,
                "prompt": f"Вставьте Past Simple (V2): {v1} — ___ — {v3}",
                "options": _options(v2, pool, "secondary_text", deck_cards),
                "speak": v1,
                "target": "v2",
                "example": card.example or None,
            }
        if kind == "choice_v3":
            return {
                "uid": f"v3-{card.id}",
                "id": card.id,
                "kind": kind,
                "prompt": f"Вставьте Past Participle (V3): {v1} — {v2} — ___",
                "options": _options(v3, pool, "tertiary_text", deck_cards),
                "speak": v1,
                "target": "v3",
                "example": card.example or None,
            }
        if kind == "choice_forms":
            pair = _form_pair(card)
            return {
                "uid": f"forms-{card.id}",
                "id": card.id,
                "kind": kind,
                "prompt": f"Какие V2 и V3 у «{v1}» ({card.translation})?",
                "options": _form_pair_options(pair, pool, deck_cards),
                "speak": v1,
                "target": "forms",
                "example": card.example or None,
            }
        if kind == "type_v2":
            return {
                "uid": f"type-v2-{card.id}",
                "id": card.id,
                "kind": kind,
                "prompt": f"Напишите Past Simple (V2) для «{v1}»",
                "options": None,
                "speak": v1,
                "target": "v2",
                "example": card.example or None,
                "input_script": "latin",
            }
        if kind == "type_v3":
            return {
                "uid": f"type-v3-{card.id}",
                "id": card.id,
                "kind": kind,
                "prompt": f"Напишите Past Participle (V3) для «{v1}»",
                "options": None,
                "speak": v1,
                "target": "v3",
                "example": card.example or None,
                "input_script": "latin",
            }

    if kind == "choice_en_ru":
        return {
            "uid": f"enru-{card.id}",
            "id": card.id,
            "kind": kind,
            "prompt": f"Как переводится «{card.primary_text}»?",
            "options": _options(card.translation, pool, "translation", deck_cards),
            "speak": _card_speak(card, deck_kind),
            "target": "translation",
            "example": card.example or None,
        }
    return {
        "uid": f"ruen-{card.id}",
        "id": card.id,
        "kind": kind,
        "prompt": f"Как по-английски: «{card.translation}»?",
        "options": _options(card.primary_text, pool, "primary_text", deck_cards),
        "target": "primary",
        "example": card.example or None,
    }


def _interleave_shuffle(items: list[dict]) -> list[dict]:
    by_card: dict[int, list[dict]] = defaultdict(list)
    for item in items:
        by_card[item["id"]].append(item)
    for bucket in by_card.values():
        random.shuffle(bucket)

    card_ids = list(by_card.keys())
    random.shuffle(card_ids)
    result: list[dict] = []
    last_id: int | None = None
    remaining = sum(len(bucket) for bucket in by_card.values())
    while remaining:
        candidates = [cid for cid in card_ids if by_card[cid] and cid != last_id]
        if not candidates:
            candidates = [cid for cid in card_ids if by_card[cid]]
        cid = random.choice(candidates)
        result.append(by_card[cid].pop())
        last_id = cid
        remaining -= 1
    return result


def _make_items(
    batch_cards: list[StudyCard],
    deck_cards: list[StudyCard],
    strength: dict[int, int],
    mastery: dict[int, int],
    deck_kind: str,
    *,
    ignore_progress: bool = False,
) -> list[dict]:
    """Queue only missing mastery facets.

    Idioms/exceptions still below strength target get a full new pass once both
    meaning sides are already done. Verbs never strength-grind: done when all
    required facets (meaning + V2/V3) are correct once.

    ignore_progress=True rebuilds a full facet set for voluntary batch replay
    without clearing stored mastery until the user actually misses.
    """
    pending: list[dict] = []
    pool = batch_cards if len(batch_cards) >= 4 else deck_cards
    kinds = _task_kinds_for(deck_kind)
    for card in batch_cards:
        flags = 0 if ignore_progress else int(mastery.get(card.id, 0) or 0)
        power = 0 if ignore_progress else int(strength.get(card.id, 0) or 0)
        if _is_learned(power, flags, deck_kind):
            continue
        # Weak idioms/exceptions that finished the meaning pass → re-queue both sides.
        needs_new_pass = (
            deck_kind != "verbs"
            and _pass_complete(flags, deck_kind)
            and not _is_learned(power, flags, deck_kind)
        )
        effective = 0 if needs_new_pass else flags
        card_kinds = list(kinds)
        random.shuffle(card_kinds)
        for kind in card_kinds:
            bit = MASTERY_BITS.get(kind, 0)
            if bit and (effective & bit):
                continue
            pending.append(_build_task(card, kind, pool, deck_cards, deck_kind))
    return _interleave_shuffle(pending)


def _slash_parts(value: str) -> list[str]:
    parts = [p.strip() for p in (value or "").split("/") if p.strip()]
    return parts or ([value] if value else [])


def _expected_for(card: StudyCard, kind: str, target: str | None) -> tuple[str, list[str]]:
    """Return (canonical target, accepted variants)."""
    if kind in {"type_v2", "choice_v2"} or target == "v2":
        field = (card.secondary_text or "").strip()
        parts = _slash_parts(field)
        accepted = list({*parts, field} - {""})
        return field or (parts[0] if parts else ""), accepted or [field]
    if kind in {"type_v3", "choice_v3"} or target == "v3":
        field = (card.tertiary_text or "").strip()
        parts = _slash_parts(field)
        accepted = list({*parts, field} - {""})
        return field or (parts[0] if parts else ""), accepted or [field]
    if kind == "choice_forms" or target == "forms":
        pair = _form_pair(card)
        return pair, [pair]
    if kind in {"choice_ru_en"} or target == "primary":
        return card.primary_text, [card.primary_text]
    # choice_en_ru / choice_translation / type_translation / default
    return card.translation, [card.translation]


def _touch_progress(
    db: Session,
    user: User,
    card: StudyCard,
    correct: bool,
    kind: str,
    deck_kind: str = "",
) -> StudyProgress:
    progress = (
        db.query(StudyProgress)
        .filter(StudyProgress.user_id == user.id, StudyProgress.card_id == card.id)
        .first()
    )
    if not progress:
        progress = StudyProgress(user_id=user.id, card_id=card.id, strength=0, mastery=0)
        db.add(progress)

    bit = MASTERY_BITS.get(kind, 0)
    if correct:
        gained_bit = False
        if bit:
            before = int(progress.mastery or 0)
            if not (before & bit):
                progress.mastery = before | bit
                gained_bit = True
        if deck_kind == "verbs":
            # Strength is display-only for verbs; mirror mastery bit count.
            progress.strength = min(
                STRENGTH_TARGET,
                _mastery_count(int(progress.mastery or 0), deck_kind),
            )
            if gained_bit:
                touch_user(db, user, 5)
        else:
            progress.strength = min(STRENGTH_TARGET, progress.strength + 1)
            touch_user(db, user, 5)
    else:
        # Miss clears direction/form flags so the next run regenerates required tasks.
        progress.mastery = 0
        progress.strength = max(0, progress.strength - 1)
    progress.last_reviewed = datetime.now(timezone.utc)
    return progress


def _parse_card_ids(raw: str | None) -> set[int] | None:
    if not raw or not raw.strip():
        return None
    ids: set[int] = set()
    for part in raw.split(","):
        part = part.strip()
        if part.isdigit():
            ids.add(int(part))
    return ids or None


@router.post("/cards/{card_id}/check")
def check_card(
    card_id: int,
    payload: StudyCheckIn,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    card = db.get(StudyCard, card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Карточка не найдена")

    deck = db.get(StudyDeck, card.deck_id)
    deck_kind = deck.kind if deck else ""

    kind = payload.kind or ""
    expected, accepted = _expected_for(card, kind, payload.target)
    if payload.accepted:
        accepted = list({*accepted, *[a for a in payload.accepted if a]})

    remembered = payload.remembered
    if remembered is not None:
        correct = bool(remembered)
    else:
        correct = is_correct(payload.answer, expected, accepted)

    progress = _touch_progress(db, user, card, correct, kind, deck_kind)
    db.commit()
    db.refresh(progress)
    mastery_value = int(progress.mastery or 0)
    return {
        "correct": correct,
        "expected": expected if not correct else None,
        "strength": progress.strength,
        "mastery": mastery_value,
        "mastery_count": _mastery_count(mastery_value, deck_kind),
        "mastery_total": _mastery_total(deck_kind),
        "learned": _is_learned(progress.strength, mastery_value, deck_kind),
        "primary_text": card.primary_text,
        "secondary_text": card.secondary_text,
        "tertiary_text": card.tertiary_text,
        "translation": card.translation,
        "example": card.example,
        # VocabSession-compatible aliases
        "word": card.primary_text,
    }


@router.get("/{kind}")
def list_decks(kind: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if kind not in KINDS:
        raise HTTPException(status_code=404, detail="Раздел не найден")
    decks = (
        db.query(StudyDeck)
        .filter(StudyDeck.kind == kind)
        .order_by(StudyDeck.sort_order, StudyDeck.id)
        .all()
    )
    result = []
    for deck in decks:
        cards = _cards(db, deck)
        strength, mastery = _progress_maps(db, user.id, [c.id for c in cards])
        learned = sum(
            1 for c in cards if _is_learned(strength.get(c.id, 0), mastery.get(c.id, 0), deck.kind)
        )
        result.append(
            {
                "id": deck.id,
                "slug": deck.slug,
                "title": deck.title,
                "description": deck.description,
                "kind": deck.kind,
                "card_count": len(cards),
                "learned_count": learned,
                "batch_count": _batch_count(len(cards)),
                "suggested_batch": _suggested_batch(cards, strength, mastery, deck.kind),
            }
        )
    return result


@router.get("/{kind}/{slug}")
def get_deck(
    kind: str,
    slug: str,
    batch: int | None = Query(default=None, ge=1),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    if kind not in KINDS:
        raise HTTPException(status_code=404, detail="Раздел не найден")
    deck = db.query(StudyDeck).filter(StudyDeck.kind == kind, StudyDeck.slug == slug).first()
    if not deck:
        raise HTTPException(status_code=404, detail="Колода не найдена")
    cards = _cards(db, deck)
    strength, mastery = _progress_maps(db, user.id, [c.id for c in cards])
    batches = _batch_count(len(cards))
    batch_index = batch or _suggested_batch(cards, strength, mastery, deck.kind)
    batch_index = min(max(1, batch_index), batches)
    chunk = cards[(batch_index - 1) * BATCH_SIZE : batch_index * BATCH_SIZE]
    learned = sum(
        1 for c in cards if _is_learned(strength.get(c.id, 0), mastery.get(c.id, 0), deck.kind)
    )
    batch_learned = sum(
        1 for c in chunk if _is_learned(strength.get(c.id, 0), mastery.get(c.id, 0), deck.kind)
    )
    return {
        "slug": deck.slug,
        "title": deck.title,
        "description": deck.description,
        "kind": deck.kind,
        "card_count": len(cards),
        "learned_count": learned,
        "batch_size": BATCH_SIZE,
        "batch_index": batch_index,
        "batch_count": batches,
        "batch_learned": batch_learned,
        "suggested_batch": _suggested_batch(cards, strength, mastery, deck.kind),
        "cards": [
            _card_out(c, strength.get(c.id, 0), mastery.get(c.id, 0), deck.kind) for c in chunk
        ],
    }


@router.get("/{kind}/{slug}/practice")
def practice_deck(
    kind: str,
    slug: str,
    batch: int | None = Query(default=None, ge=1),
    cards: str | None = Query(default=None, description="Comma-separated card ids to redo"),
    replay: bool = Query(default=False, description="Full voluntary replay of the batch"),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    if kind not in KINDS:
        raise HTTPException(status_code=404, detail="Раздел не найден")
    deck = db.query(StudyDeck).filter(StudyDeck.kind == kind, StudyDeck.slug == slug).first()
    if not deck:
        raise HTTPException(status_code=404, detail="Колода не найдена")
    all_cards = _cards(db, deck)
    strength, mastery = _progress_maps(db, user.id, [c.id for c in all_cards])
    batch_count = _batch_count(len(all_cards))
    batch_index = min(batch or _suggested_batch(all_cards, strength, mastery, deck.kind), batch_count)
    batch_index = max(1, batch_index)
    chunk = all_cards[(batch_index - 1) * BATCH_SIZE : batch_index * BATCH_SIZE]
    id_filter = _parse_card_ids(cards)
    batch_complete = bool(chunk) and all(
        _is_learned(strength.get(c.id, 0), mastery.get(c.id, 0), deck.kind) for c in chunk
    )
    # Failed-item redo keeps mastery as stored (miss already cleared bits).
    # Explicit replay — or practice on an already-closed batch — rebuilds all facets.
    do_replay = bool(replay or (id_filter is None and batch_complete))
    if id_filter is not None:
        pending_cards = [c for c in chunk if c.id in id_filter]
        items = _make_items(pending_cards, all_cards, strength, mastery, deck.kind)
    elif do_replay:
        pending_cards = list(chunk)
        items = _make_items(
            pending_cards, all_cards, strength, mastery, deck.kind, ignore_progress=True
        )
    else:
        pending_cards = [
            c
            for c in chunk
            if not _is_learned(strength.get(c.id, 0), mastery.get(c.id, 0), deck.kind)
        ]
        items = _make_items(pending_cards, all_cards, strength, mastery, deck.kind)
    learned = sum(
        1 for c in all_cards if _is_learned(strength.get(c.id, 0), mastery.get(c.id, 0), deck.kind)
    )
    batch_learned = sum(
        1 for c in chunk if _is_learned(strength.get(c.id, 0), mastery.get(c.id, 0), deck.kind)
    )
    return {
        "deck": {"slug": deck.slug, "title": deck.title, "kind": deck.kind},
        "batch_index": batch_index,
        "batch_count": batch_count,
        "card_count": len(all_cards),
        "learned_count": learned,
        "batch_learned": batch_learned,
        "batch_card_count": len(chunk),
        "pending_tasks": len(items),
        "cards": [
            _card_out(c, strength.get(c.id, 0), mastery.get(c.id, 0), deck.kind) for c in pending_cards
        ],
        "items": items,
    }
