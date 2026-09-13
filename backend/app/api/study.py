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

# Both-direction mastery — card is learned when mastery == LEARNED_MASTERY.
MASTERY_BITS = {
    "choice_en_ru": 1,
    "choice_ru_en": 2,
    # Legacy aliases from free-text / one-way packs.
    "choice_translation": 1,
    "type_translation": 1,
}
LEARNED_MASTERY = 3
TASK_KINDS = ("choice_en_ru", "choice_ru_en")


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


def _is_learned(mastery_value: int) -> bool:
    return (mastery_value & LEARNED_MASTERY) == LEARNED_MASTERY


def _mastery_count(mastery_value: int) -> int:
    return bin(mastery_value & LEARNED_MASTERY).count("1")


def _suggested_batch(cards: list[StudyCard], mastery: dict[int, int]) -> int:
    n = _batch_count(len(cards))
    for index in range(n):
        chunk = cards[index * BATCH_SIZE : (index + 1) * BATCH_SIZE]
        if any(not _is_learned(mastery.get(card.id, 0)) for card in chunk):
            return index + 1
    return n


def _card_out(card: StudyCard, strength: int = 0, mastery_value: int = 0) -> dict:
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
        "mastery_count": _mastery_count(mastery_value),
        "learned": _is_learned(mastery_value),
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


def _build_task(card: StudyCard, kind: str, pool: list[StudyCard], deck_cards: list[StudyCard]) -> dict:
    if kind == "choice_en_ru":
        return {
            "uid": f"enru-{card.id}",
            "id": card.id,
            "kind": kind,
            "prompt": f"Как переводится «{card.primary_text}»?",
            "options": _options(card.translation, pool, "translation", deck_cards),
            "speak": card.primary_text.split("→")[0].strip(),
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
    mastery: dict[int, int],
) -> list[dict]:
    """Both directions for every card that is not yet fully learned."""
    pending: list[dict] = []
    pool = batch_cards if len(batch_cards) >= 4 else deck_cards
    for card in batch_cards:
        if _is_learned(mastery.get(card.id, 0)):
            continue
        kinds = list(TASK_KINDS)
        random.shuffle(kinds)
        for kind in kinds:
            pending.append(_build_task(card, kind, pool, deck_cards))
    return _interleave_shuffle(pending)


def _expected_for(card: StudyCard, kind: str, target: str | None) -> tuple[str, list[str]]:
    """Return (canonical target, accepted variants)."""
    if kind in {"type_v2"}:
        parts = [p.strip() for p in card.secondary_text.split("/") if p.strip()]
        return (parts[0] if parts else card.secondary_text, parts or [card.secondary_text])
    if kind in {"type_v3"}:
        parts = [p.strip() for p in card.tertiary_text.split("/") if p.strip()]
        return (parts[0] if parts else card.tertiary_text, parts or [card.tertiary_text])
    if kind in {"choice_ru_en"} or target == "primary":
        return card.primary_text, [card.primary_text]
    # choice_en_ru / choice_translation / type_translation / default
    return card.translation, [card.translation]


def _touch_progress(db: Session, user: User, card: StudyCard, correct: bool, kind: str) -> StudyProgress:
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
        if bit:
            before = int(progress.mastery or 0)
            if not (before & bit):
                progress.mastery = before | bit
        progress.strength = min(5, progress.strength + 1)
        touch_user(db, user, 5)
    else:
        # Miss clears direction flags so the next run regenerates both tasks.
        progress.mastery = 0
        progress.strength = max(0, progress.strength - 1)
    progress.last_reviewed = datetime.now(timezone.utc)
    return progress


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

    kind = payload.kind or ""
    expected, accepted = _expected_for(card, kind, payload.target)
    if payload.accepted:
        accepted = list({*accepted, *[a for a in payload.accepted if a]})

    remembered = payload.remembered
    if remembered is not None:
        correct = bool(remembered)
    else:
        correct = is_correct(payload.answer, expected, accepted)

    progress = _touch_progress(db, user, card, correct, kind)
    db.commit()
    mastery_value = int(progress.mastery or 0)
    return {
        "correct": correct,
        "expected": expected if not correct else None,
        "strength": progress.strength,
        "mastery": mastery_value,
        "mastery_count": _mastery_count(mastery_value),
        "learned": _is_learned(mastery_value),
        "primary_text": card.primary_text,
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
        _, mastery = _progress_maps(db, user.id, [c.id for c in cards])
        learned = sum(1 for c in cards if _is_learned(mastery.get(c.id, 0)))
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
                "suggested_batch": _suggested_batch(cards, mastery),
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
    batch_index = batch or _suggested_batch(cards, mastery)
    batch_index = min(max(1, batch_index), batches)
    chunk = cards[(batch_index - 1) * BATCH_SIZE : batch_index * BATCH_SIZE]
    learned = sum(1 for c in cards if _is_learned(mastery.get(c.id, 0)))
    batch_learned = sum(1 for c in chunk if _is_learned(mastery.get(c.id, 0)))
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
        "suggested_batch": _suggested_batch(cards, mastery),
        "cards": [
            _card_out(c, strength.get(c.id, 0), mastery.get(c.id, 0)) for c in chunk
        ],
    }


@router.get("/{kind}/{slug}/practice")
def practice_deck(
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
    batch_count = _batch_count(len(cards))
    batch_index = min(batch or _suggested_batch(cards, mastery), batch_count)
    batch_index = max(1, batch_index)
    chunk = cards[(batch_index - 1) * BATCH_SIZE : batch_index * BATCH_SIZE]
    pending_cards = [c for c in chunk if not _is_learned(mastery.get(c.id, 0))]
    items = _make_items(pending_cards, cards, mastery)
    learned = sum(1 for c in cards if _is_learned(mastery.get(c.id, 0)))
    batch_learned = sum(1 for c in chunk if _is_learned(mastery.get(c.id, 0)))
    return {
        "deck": {"slug": deck.slug, "title": deck.title, "kind": deck.kind},
        "batch_index": batch_index,
        "batch_count": batch_count,
        "card_count": len(cards),
        "learned_count": learned,
        "batch_learned": batch_learned,
        "batch_card_count": len(chunk),
        "pending_tasks": len(items),
        "cards": [
            _card_out(c, strength.get(c.id, 0), mastery.get(c.id, 0)) for c in pending_cards
        ],
        "items": items,
    }
