from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.grammar import Exercise, GrammarLevel, GrammarModule, Lesson
from app.models.progress import ExerciseAttempt, ModuleProgress
from app.models.user import User

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
        completed = sum(1 for m in modules if progress.get(m.id) and progress[m.id].status == "completed")
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
                "progress": {
                    "status": progress[module.id].status if module.id in progress else "not_started",
                    "lesson_done": progress[module.id].lesson_done if module.id in progress else False,
                    "practice_score": progress[module.id].practice_score if module.id in progress else 0,
                    "test_score": progress[module.id].test_score if module.id in progress else None,
                },
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
        "progress": {
            "status": progress.status if progress else "not_started",
            "lesson_done": progress.lesson_done if progress else False,
            "practice_score": progress.practice_score if progress else 0,
            "test_score": progress.test_score if progress else None,
        },
    }


@router.get("/modules/{slug}/lessons/{lesson_id}")
def get_lesson(
    slug: str,
    lesson_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    lesson = (
        db.query(Lesson)
        .options(joinedload(Lesson.module))
        .filter(Lesson.id == lesson_id)
        .first()
    )
    if not lesson or lesson.module.slug != slug:
        raise HTTPException(status_code=404, detail="Урок не найден")
    from app.services.scoring import get_or_create_progress

    progress = get_or_create_progress(db, user.id, lesson.module_id)
    progress.lesson_done = True
    if progress.status == "not_started":
        progress.status = "in_progress"
    db.commit()
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
    solved = {
        row.exercise_id
        for row in db.query(ExerciseAttempt)
        .filter(ExerciseAttempt.user_id == user.id, ExerciseAttempt.is_correct.is_(True))
        .all()
    }
    exercises = (
        db.query(Exercise).filter(Exercise.module_id == module.id).order_by(Exercise.sort_order).all()
    )
    return {
        "module": {"id": module.id, "slug": module.slug, "title": module.title},
        "exercises": [
            {
                "id": item.id,
                "kind": item.kind,
                "prompt": item.prompt,
                "options": _practice_options(item),
                "sort_order": item.sort_order,
                "xp": item.xp,
                "solved": item.id in solved,
            }
            for item in exercises
        ],
    }
