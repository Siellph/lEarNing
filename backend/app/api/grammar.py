from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.grammar import Exercise, GrammarLevel, GrammarModule, Lesson
from app.models.progress import ExerciseAttempt, ModuleProgress
from app.models.user import User
from app.services.scoring import effective_module_status

router = APIRouter(prefix="/grammar", tags=["grammar"])


def _practice_options(item):
    if item.kind == "match":
        from app.services.match_format import public_match_options

        sides = public_match_options(item.options, item.answer)
        if sides:
            return sides
    return item.options


def _progress_map(db: Session, user_id: int) -> dict[int, ModuleProgress]:
    rows = db.query(ModuleProgress).filter(ModuleProgress.user_id == user_id).all()
    return {row.module_id: row for row in rows}


def _public_progress(progress: ModuleProgress | None) -> dict:
    return {
        "status": effective_module_status(progress),
        # Theory is reading-only; never surface lesson completion to the client.
        "lesson_done": False,
        "practice_score": progress.practice_score if progress else 0,
        "test_score": progress.test_score if progress else None,
    }


@router.get("/levels")
def list_levels(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    levels = db.query(GrammarLevel).order_by(GrammarLevel.sort_order).all()
    progress = _progress_map(db, user.id)
    result = []
    for level in levels:
        modules = (
            db.query(GrammarModule)
            .filter(GrammarModule.level_id == level.id)
            .order_by(GrammarModule.sort_order)
            .all()
        )
        completed = sum(1 for m in modules if effective_module_status(progress.get(m.id)) == "completed")
        result.append(
            {
                "id": level.id,
                "code": level.code,
                "title": level.title,
                "subtitle": level.subtitle,
                "description": level.description,
                "sort_order": level.sort_order,
                "module_count": len(modules),
                "completed_count": completed,
            }
        )
    return result


@router.get("/levels/{code}/modules")
def list_modules(code: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    level = db.query(GrammarLevel).filter(GrammarLevel.code == code.upper()).first()
    if not level:
        raise HTTPException(status_code=404, detail="Уровень не найден")
    modules = (
        db.query(GrammarModule)
        .filter(GrammarModule.level_id == level.id)
        .order_by(GrammarModule.sort_order)
        .all()
    )
    progress = _progress_map(db, user.id)
    return {
        "level": {
            "id": level.id,
            "code": level.code,
            "title": level.title,
            "subtitle": level.subtitle,
            "description": level.description,
        },
        "modules": [
            {
                "id": module.id,
                "slug": module.slug,
                "title": module.title,
                "description": module.description,
                "sort_order": module.sort_order,
                "estimated_minutes": module.estimated_minutes,
                "sources": module.sources,
                "exercise_count": len(module.exercises),
                "has_test": module.test is not None,
                "progress": _public_progress(progress.get(module.id)),
            }
            for module in modules
        ],
    }


@router.get("/modules/{slug}")
def get_module(slug: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    module = (
        db.query(GrammarModule)
        .options(joinedload(GrammarModule.level), joinedload(GrammarModule.lessons), joinedload(GrammarModule.test))
        .filter(GrammarModule.slug == slug)
        .first()
    )
    if not module:
        raise HTTPException(status_code=404, detail="Модуль не найден")
    progress = (
        db.query(ModuleProgress)
        .filter(ModuleProgress.user_id == user.id, ModuleProgress.module_id == module.id)
        .first()
    )
    lessons = sorted(module.lessons, key=lambda item: item.sort_order)
    return {
        "id": module.id,
        "slug": module.slug,
        "title": module.title,
        "description": module.description,
        "estimated_minutes": module.estimated_minutes,
        "sources": module.sources,
        "level": {"code": module.level.code, "title": module.level.title},
        "lessons": [{"id": lesson.id, "title": lesson.title, "sort_order": lesson.sort_order} for lesson in lessons],
        "exercise_count": len(module.exercises),
        "test": (
            {
                "id": module.test.id,
                "title": module.test.title,
                "time_limit_sec": module.test.time_limit_sec,
                "passing_score": module.test.passing_score,
                "question_count": len(module.test.questions),
            }
            if module.test
            else None
        ),
        "progress": _public_progress(progress),
    }


@router.get("/modules/{slug}/lessons/{lesson_id}")
def get_lesson(
    slug: str,
    lesson_id: int,
    db: Session = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    lesson = (
        db.query(Lesson)
        .options(joinedload(Lesson.module))
        .filter(Lesson.id == lesson_id)
        .first()
    )
    if not lesson or lesson.module.slug != slug:
        raise HTTPException(status_code=404, detail="Урок не найден")
    # Theory is reading material only — do not mark lesson/module progress here.
    return {
        "id": lesson.id,
        "title": lesson.title,
        "content": lesson.content,
        "module": {"slug": lesson.module.slug, "title": lesson.module.title},
    }


@router.get("/modules/{slug}/practice")
def get_practice(slug: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    module = db.query(GrammarModule).filter(GrammarModule.slug == slug).first()
    if not module:
        raise HTTPException(status_code=404, detail="Модуль не найден")
    exercises = (
        db.query(Exercise).filter(Exercise.module_id == module.id).order_by(Exercise.sort_order).all()
    )
    exercise_ids = [item.id for item in exercises]
    last_by_exercise: dict[int, ExerciseAttempt] = {}
    solved: set[int] = set()
    if exercise_ids:
        attempts = (
            db.query(ExerciseAttempt)
            .filter(
                ExerciseAttempt.user_id == user.id,
                ExerciseAttempt.exercise_id.in_(exercise_ids),
            )
            .order_by(ExerciseAttempt.id.desc())
            .all()
        )
        for attempt in attempts:
            if attempt.exercise_id not in last_by_exercise:
                last_by_exercise[attempt.exercise_id] = attempt
            if attempt.is_correct:
                solved.add(attempt.exercise_id)

    payload_exercises = []
    for item in exercises:
        last = last_by_exercise.get(item.id)
        last_result = None
        if last:
            # Match needs `expected` even when correct so the UI can refill slots
            # if the stored attempt string is empty or uses shortened left keys.
            show_expected = (not last.is_correct) or item.kind == "match"
            last_result = {
                "correct": last.is_correct,
                "explanation": item.explanation or "",
                "expected": item.answer if show_expected else None,
                "answer": last.answer,
            }
        payload_exercises.append(
            {
                "id": item.id,
                "kind": item.kind,
                "prompt": item.prompt,
                "options": _practice_options(item),
                "sort_order": item.sort_order,
                "xp": item.xp,
                "solved": item.id in solved,
                "last_result": last_result,
            }
        )

    return {
        "module": {"id": module.id, "slug": module.slug, "title": module.title},
        "exercises": payload_exercises,
    }
