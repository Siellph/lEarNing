from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.grammar import Exam, GrammarLevel, GrammarModule
from app.models.progress import ExamAttempt, ExerciseAttempt, ModuleProgress, TestAttempt
from app.models.user import User
from app.models.vocabulary import VocabProgress, VocabWord

router = APIRouter(prefix="/progress", tags=["progress"])


@router.get("/me")
def my_progress(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    levels = db.query(GrammarLevel).order_by(GrammarLevel.sort_order).all()
    progress_rows = db.query(ModuleProgress).filter(ModuleProgress.user_id == user.id).all()
    progress_map = {row.module_id: row for row in progress_rows}
    by_level = []
    completed_total = 0
    module_total = 0
    for level in levels:
        modules = (
            db.query(GrammarModule)
            .filter(GrammarModule.level_id == level.id)
            .order_by(GrammarModule.sort_order)
            .all()
        )
        completed = sum(1 for m in modules if progress_map.get(m.id) and progress_map[m.id].status == "completed")
        completed_total += completed
        module_total += len(modules)
        by_level.append(
            {
                "code": level.code,
                "title": level.title,
                "completed": completed,
                "total": len(modules),
            }
        )

    correct_attempts = (
        db.query(func.count(ExerciseAttempt.id))
        .filter(ExerciseAttempt.user_id == user.id, ExerciseAttempt.is_correct.is_(True))
        .scalar()
        or 0
    )
    tests_passed = (
        db.query(func.count(TestAttempt.id))
        .filter(
            TestAttempt.user_id == user.id,
            TestAttempt.passed.is_(True),
            TestAttempt.status == "submitted",
        )
        .scalar()
        or 0
    )
    exams_passed = (
        db.query(func.count(func.distinct(ExamAttempt.exam_id)))
        .filter(
            ExamAttempt.user_id == user.id,
            ExamAttempt.passed.is_(True),
            ExamAttempt.status == "submitted",
        )
        .scalar()
        or 0
    )
    vocab_learned = (
        db.query(func.count(VocabProgress.id))
        .filter(VocabProgress.user_id == user.id, VocabProgress.mastery >= 15)
        .scalar()
        or 0
    )
    vocab_total = db.query(func.count(VocabWord.id)).scalar() or 0
    exam_total = db.query(func.count(Exam.id)).scalar() or 0

    recent_tests = (
        db.query(TestAttempt)
        .filter(TestAttempt.user_id == user.id, TestAttempt.status == "submitted")
        .order_by(TestAttempt.created_at.desc())
        .limit(5)
        .all()
    )
    recent_exams = (
        db.query(ExamAttempt)
        .filter(ExamAttempt.user_id == user.id, ExamAttempt.status == "submitted")
        .order_by(ExamAttempt.created_at.desc())
        .limit(5)
        .all()
    )

    return {
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "xp": user.xp,
            "streak": user.streak,
        },
        "modules": {"completed": completed_total, "total": module_total},
        "by_level": by_level,
        "practice_correct": correct_attempts,
        "tests_passed": tests_passed,
        "exams": {"passed": exams_passed, "total": exam_total},
        "vocab": {"learned": vocab_learned, "total": vocab_total},
        "recent": {
            "tests": [{"id": t.id, "score": t.score, "passed": t.passed, "created_at": t.created_at} for t in recent_tests],
            "exams": [{"id": e.id, "score": e.score, "passed": e.passed, "created_at": e.created_at} for e in recent_exams],
        },
    }
