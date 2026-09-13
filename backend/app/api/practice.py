from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.grammar import Exercise
from app.models.progress import ExerciseAttempt
from app.models.user import User
from app.schemas.content import AnswerIn
from app.services.scoring import get_or_create_progress, is_correct, refresh_module_status, touch_user

router = APIRouter(prefix="/practice", tags=["practice"])


@router.post("/exercises/{exercise_id}/check")
def check_exercise(
    exercise_id: int,
    payload: AnswerIn,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    exercise = db.get(Exercise, exercise_id)
    if not exercise:
        raise HTTPException(status_code=404, detail="Упражнение не найдено")

    correct = is_correct(payload.answer, exercise.answer, exercise.accepted, prompt=exercise.prompt)
    already = (
        db.query(ExerciseAttempt)
        .filter(
            ExerciseAttempt.user_id == user.id,
            ExerciseAttempt.exercise_id == exercise.id,
            ExerciseAttempt.is_correct.is_(True),
        )
        .count()
    )
    attempt = ExerciseAttempt(
        user_id=user.id,
        exercise_id=exercise.id,
        answer=payload.answer,
        is_correct=correct,
    )
    db.add(attempt)

    awarded = 0
    if correct:
        if already == 0:
            awarded = exercise.xp
            touch_user(db, user, awarded)
        progress = get_or_create_progress(db, user.id, exercise.module_id)
        db.flush()
        total = db.query(Exercise).filter(Exercise.module_id == exercise.module_id).count()
        solved = (
            db.query(ExerciseAttempt.exercise_id)
            .filter(
                ExerciseAttempt.user_id == user.id,
                ExerciseAttempt.is_correct.is_(True),
                ExerciseAttempt.exercise_id.in_(
                    db.query(Exercise.id).filter(Exercise.module_id == exercise.module_id)
                ),
            )
            .distinct()
            .count()
        )
        progress.practice_score = round(solved * 100 / total) if total else 0
        refresh_module_status(progress)

    db.commit()
    return {
        "correct": correct,
        "explanation": exercise.explanation,
        "expected": exercise.answer if not correct else None,
        "xp_awarded": awarded,
    }
