"""Study decks API: irregular verbs, idioms, exceptions (vocab-like batches)."""

import math
import random
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
LEARNED_STRENGTH = 3
KINDS = {"verbs", "idioms", "exceptions"}


def _cards(db: Session, deck: StudyDeck) -> list[StudyCard]:
    return db.query(StudyCard).filter(StudyCard.deck_id == deck.id).order_by(StudyCard.sort_order, StudyCard.id).all()


def _strength_map(db: Session, user_id: int, card_ids: list[int]) -> dict[int, int]:
    if not card_ids:
        return {}
    rows = (
        db.query(StudyProgress)
        .filter(StudyProgress.user_id == user_id, StudyProgress.card_id.in_(card_ids))
        .all()
    )
    return {row.card_id: row.strength for row in rows}


def _batch_count(total: int) -> int:
    return max(1, math.ceil(total / BATCH_SIZE)) if total else 1


def _suggested_batch(cards: list[StudyCard], strength: dict[int, int]) -> int:
    n = _batch_count(len(cards))
    for index in range(n):
        chunk = cards[index * BATCH_SIZE : (index + 1) * BATCH_SIZE]
        if any(strength.get(card.id, 0) < LEARNED_STRENGTH for card in chunk):
            return index + 1
    return n


def _card_out(card: StudyCard, strength: int = 0) -> dict:
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
    }


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
    target = (payload.target or "").strip()
    accepted = payload.accepted or []
    if payload.kind in {"type_v2"}:
        target = card.secondary_text.split("/")[0].strip()
        accepted = [p.strip() for p in card.secondary_text.split("/")]
    elif payload.kind in {"type_v3"}:
        target = card.tertiary_text.split("/")[0].strip()
        accepted = [p.strip() for p in card.tertiary_text.split("/")]
    elif payload.kind in {"choice_translation", "type_translation"} or not target:
        target = card.translation
        accepted = [card.translation]

    remembered = payload.remembered
    if remembered is not None:
        correct = bool(remembered)
    else:
        correct = is_correct(payload.answer, target, accepted)

    progress = (
        db.query(StudyProgress)
        .filter(StudyProgress.user_id == user.id, StudyProgress.card_id == card.id)
        .first()
    )
    if not progress:
        progress = StudyProgress(user_id=user.id, card_id=card.id, strength=0)
        db.add(progress)
    if correct:
        progress.strength = min(5, progress.strength + 1)
        touch_user(db, user, 5)
    else:
        progress.strength = max(0, progress.strength - 1)
    progress.last_reviewed = datetime.now(timezone.utc)
    db.commit()
    return {
        "correct": correct,
        "expected": target if not correct else None,
        "strength": progress.strength,
        "primary_text": card.primary_text,
        "translation": card.translation,
        "example": card.example,
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
        strength = _strength_map(db, user.id, [c.id for c in cards])
        learned = sum(1 for c in cards if strength.get(c.id, 0) >= LEARNED_STRENGTH)
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
                "suggested_batch": _suggested_batch(cards, strength),
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
    strength = _strength_map(db, user.id, [c.id for c in cards])
    batches = _batch_count(len(cards))
    batch_index = batch or _suggested_batch(cards, strength)
    batch_index = min(max(1, batch_index), batches)
    chunk = cards[(batch_index - 1) * BATCH_SIZE : batch_index * BATCH_SIZE]
    learned = sum(1 for c in cards if strength.get(c.id, 0) >= LEARNED_STRENGTH)
    batch_learned = sum(1 for c in chunk if strength.get(c.id, 0) >= LEARNED_STRENGTH)
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
        "suggested_batch": _suggested_batch(cards, strength),
        "cards": [_card_out(c, strength.get(c.id, 0)) for c in chunk],
    }


@router.get("/{kind}/{slug}/practice")
def practice_deck(
    kind: str,
    slug: str,
    batch: int | None = Query(default=None, ge=1),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    data = get_deck(kind, slug, batch=batch, db=db, user=user)
    cards = data["cards"]
    items = []
    for card in cards:
        if kind == "verbs":
            items.append(
                {
                    "uid": f"v2-{card['id']}",
                    "id": card["id"],
                    "kind": "type_v2",
                    "prompt": f"V2 от {card['primary_text']} ({card['translation']})",
                    "target": card["secondary_text"].split("/")[0].strip(),
                    "accepted": [p.strip() for p in card["secondary_text"].split("/")],
                }
            )
            items.append(
                {
                    "uid": f"v3-{card['id']}",
                    "id": card["id"],
                    "kind": "type_v3",
                    "prompt": f"V3 от {card['primary_text']} ({card['translation']})",
                    "target": card["tertiary_text"].split("/")[0].strip(),
                    "accepted": [p.strip() for p in card["tertiary_text"].split("/")],
                }
            )
            pool = [c["translation"] for c in cards if c["id"] != card["id"]]
            opts = [card["translation"], *random.sample(pool, min(3, len(pool)))]
            random.shuffle(opts)
            items.append(
                {
                    "uid": f"tr-{card['id']}",
                    "id": card["id"],
                    "kind": "choice_translation",
                    "prompt": f"Перевод: {card['primary_text']}",
                    "options": opts,
                    "target": card["translation"],
                }
            )
        else:
            pool = [c["translation"] for c in cards if c["id"] != card["id"]]
            opts = [card["translation"], *random.sample(pool, min(3, len(pool)))]
            random.shuffle(opts)
            items.append(
                {
                    "uid": f"ch-{card['id']}",
                    "id": card["id"],
                    "kind": "choice_translation",
                    "prompt": f"Значение: {card['primary_text']}",
                    "options": opts,
                    "target": card["translation"],
                    "example": card.get("example"),
                }
            )
            items.append(
                {
                    "uid": f"ty-{card['id']}",
                    "id": card["id"],
                    "kind": "type_translation",
                    "prompt": f"Введите русский смысл: {card['primary_text']}",
                    "target": card["translation"],
                }
            )
    random.shuffle(items)
    return {
        "deck": {"slug": data["slug"], "title": data["title"], "kind": data["kind"]},
        "batch_index": data["batch_index"],
        "batch_count": data["batch_count"],
        "items": items[: max(8, min(16, len(items)))],
    }
