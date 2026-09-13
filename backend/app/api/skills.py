"""Skills API: graded reading, listening/dictation, mini-dialogues."""

from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.skills import SkillItem, SkillProgress, SkillQuestion
from app.models.user import User
from app.schemas.content import SkillCheckIn
from app.services.scoring import is_correct, touch_user

router = APIRouter(prefix="/skills", tags=["skills"])

LEARNED_STRENGTH = 3
KINDS = {"reading", "listening", "dialogue"}


def _progress_map(db: Session, user_id: int, item_ids: list[int]) -> dict[int, int]:
    if not item_ids:
        return {}
    rows = (
        db.query(SkillProgress)
        .filter(SkillProgress.user_id == user_id, SkillProgress.item_id.in_(item_ids))
        .all()
    )
    return {row.item_id: row.strength for row in rows}


def _item_summary(item: SkillItem, strength: int = 0) -> dict:
    return {
        "id": item.id,
        "slug": item.slug,
        "title": item.title,
        "description": item.description,
        "kind": item.kind,
        "level_code": item.level_code,
        "question_count": len(item.questions),
        "keyword_count": len(item.keywords or []),
        "strength": strength,
        "learned": strength >= LEARNED_STRENGTH,
    }


@router.post("/questions/{question_id}/check")
def check_question(
    question_id: int,
    payload: SkillCheckIn,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    question = db.get(SkillQuestion, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Вопрос не найден")
    item = question.item
    target = question.answer
    accepted = list(question.accepted or [])
    if target and target not in accepted:
        accepted = [target, *accepted]

    correct = is_correct(payload.answer, target, accepted)

    progress = (
        db.query(SkillProgress)
        .filter(SkillProgress.user_id == user.id, SkillProgress.item_id == item.id)
        .first()
    )
    if not progress:
        progress = SkillProgress(user_id=user.id, item_id=item.id, strength=0)
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
        "explanation": question.explanation if not correct else "",
    }


@router.get("/{kind}")
def list_items(kind: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if kind not in KINDS:
        raise HTTPException(status_code=404, detail="Раздел не найден")
    items = (
        db.query(SkillItem)
        .filter(SkillItem.kind == kind)
        .order_by(SkillItem.sort_order, SkillItem.id)
        .all()
    )
    strength = _progress_map(db, user.id, [i.id for i in items])
    return [_item_summary(item, strength.get(item.id, 0)) for item in items]


@router.get("/{kind}/{slug}")
def get_item(
    kind: str,
    slug: str,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    if kind not in KINDS:
        raise HTTPException(status_code=404, detail="Раздел не найден")
    item = db.query(SkillItem).filter(SkillItem.kind == kind, SkillItem.slug == slug).first()
    if not item:
        raise HTTPException(status_code=404, detail="Материал не найден")
    strength = _progress_map(db, user.id, [item.id]).get(item.id, 0)
    return {
        **_item_summary(item, strength),
        "body": item.body,
        "lines": item.lines or [],
        "keywords": item.keywords or [],
    }


@router.get("/{kind}/{slug}/practice")
def practice_item(
    kind: str,
    slug: str,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    if kind not in KINDS:
        raise HTTPException(status_code=404, detail="Раздел не найден")
    item = db.query(SkillItem).filter(SkillItem.kind == kind, SkillItem.slug == slug).first()
    if not item:
        raise HTTPException(status_code=404, detail="Материал не найден")
    questions = (
        db.query(SkillQuestion)
        .filter(SkillQuestion.item_id == item.id)
        .order_by(SkillQuestion.sort_order, SkillQuestion.id)
        .all()
    )
    items = []
    for q in questions:
        speak = q.speak or (item.body if q.kind == "dictation" and kind == "listening" else "")
        payload = {
            "uid": f"q-{q.id}",
            "id": q.id,
            "kind": q.kind,
            "prompt": q.prompt,
            "options": q.options,
            "speak": speak or None,
            "explanation": q.explanation,
        }
        items.append(payload)
    return {
        "item": {
            "slug": item.slug,
            "title": item.title,
            "kind": item.kind,
            "level_code": item.level_code,
        },
        "items": items,
    }
