"""Skills API: graded reading, listening/dictation, mini-dialogues."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.skills import SkillItem, SkillQuestion
from app.models.user import User
from app.schemas.content import SkillCheckIn
from app.services.scoring import is_correct

router = APIRouter(prefix="/skills", tags=["skills"])

KINDS = {"reading", "listening", "dialogue"}


def _item_summary(item: SkillItem) -> dict:
    return {
        "id": item.id,
        "slug": item.slug,
        "title": item.title,
        "description": item.description,
        "kind": item.kind,
        "level_code": item.level_code,
        "question_count": len(item.questions),
        "keyword_count": len(item.keywords or []),
    }


@router.post("/questions/{question_id}/check")
def check_question(
    question_id: int,
    payload: SkillCheckIn,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    """Score an answer only — no strength/progress persistence for skills."""
    question = db.get(SkillQuestion, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Вопрос не найден")
    target = question.answer
    accepted = list(question.accepted or [])
    if target and target not in accepted:
        accepted = [target, *accepted]

    correct = is_correct(payload.answer, target, accepted)
    return {
        "correct": correct,
        "expected": target if not correct else None,
        "explanation": question.explanation if not correct else "",
    }


@router.get("/{kind}")
def list_items(kind: str, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    if kind not in KINDS:
        raise HTTPException(status_code=404, detail="Раздел не найден")
    items = (
        db.query(SkillItem)
        .filter(SkillItem.kind == kind)
        .order_by(SkillItem.sort_order, SkillItem.id)
        .all()
    )
    return [_item_summary(item) for item in items]


@router.get("/{kind}/{slug}")
def get_item(
    kind: str,
    slug: str,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    if kind not in KINDS:
        raise HTTPException(status_code=404, detail="Раздел не найден")
    item = db.query(SkillItem).filter(SkillItem.kind == kind, SkillItem.slug == slug).first()
    if not item:
        raise HTTPException(status_code=404, detail="Материал не найден")
    return {
        **_item_summary(item),
        "body": item.body,
        "lines": item.lines or [],
        "keywords": item.keywords or [],
    }


@router.get("/{kind}/{slug}/practice")
def practice_item(
    kind: str,
    slug: str,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
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
