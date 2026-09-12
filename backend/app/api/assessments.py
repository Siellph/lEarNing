from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.grammar import Exam, GrammarModule, ModuleTest
from app.models.progress import ExamAttempt, TestAttempt
from app.models.user import User
from app.schemas.content import ExamSubmitIn, TestSubmitIn
from app.services.scoring import get_or_create_progress, is_correct, percent, refresh_module_status, touch_user

router = APIRouter(tags=["assessments"])


def _public_questions(items):
    return [
        {
            "id": item.id,
            "kind": item.kind,
            "prompt": item.prompt,
            "options": item.options,
            "sort_order": item.sort_order,
        }
        for item in sorted(items, key=lambda q: q.sort_order)
    ]


@router.get("/tests/{test_id}")
def get_test(test_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    test = (
        db.query(ModuleTest)
        .options(joinedload(ModuleTest.module), joinedload(ModuleTest.questions))
        .filter(ModuleTest.id == test_id)
        .first()
    )
    if not test:
        raise HTTPException(status_code=404, detail="Тест не найден")
    last = (
        db.query(TestAttempt)
        .filter(TestAttempt.user_id == user.id, TestAttempt.test_id == test.id)
        .order_by(TestAttempt.created_at.desc())
        .first()
    )
    return {
        "id": test.id,
        "title": test.title,
        "time_limit_sec": test.time_limit_sec,
        "passing_score": test.passing_score,
        "module": {"slug": test.module.slug, "title": test.module.title},
        "questions": _public_questions(test.questions),
        "last_attempt": {"score": last.score, "passed": last.passed} if last else None,
    }


@router.post("/tests/{test_id}/submit")
def submit_test(
    test_id: int,
    payload: TestSubmitIn,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    test = (
        db.query(ModuleTest)
        .options(joinedload(ModuleTest.questions))
        .filter(ModuleTest.id == test_id)
        .first()
    )
    if not test:
        raise HTTPException(status_code=404, detail="Тест не найден")
    details = []
    correct_n = 0
    for question in test.questions:
        given = payload.answers.get(str(question.id), "")
        ok = is_correct(given, question.answer, question.accepted)
        if ok:
            correct_n += 1
        details.append(
            {
                "id": question.id,
                "prompt": question.prompt,
                "given": given,
                "correct": ok,
                "expected": question.answer,
                "explanation": question.explanation,
            }
        )
    score = percent(correct_n, len(test.questions))
    passed = score >= test.passing_score
    attempt = TestAttempt(
        user_id=user.id,
        test_id=test.id,
        score=score,
        passed=passed,
        answers=payload.answers,
    )
    db.add(attempt)
    progress = get_or_create_progress(db, user.id, test.module_id)
    if progress.test_score is None or score > progress.test_score:
        progress.test_score = score
    refresh_module_status(progress)
    if passed:
        touch_user(db, user, 40)
    db.commit()
    return {"score": score, "passed": passed, "passing_score": test.passing_score, "details": details}


@router.get("/exams")
def list_exams(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    exams = db.query(Exam).options(joinedload(Exam.level)).order_by(Exam.id).all()
    attempts = (
        db.query(ExamAttempt)
        .filter(ExamAttempt.user_id == user.id)
        .order_by(ExamAttempt.created_at.desc())
        .all()
    )
    latest = {}
    for attempt in attempts:
        latest.setdefault(attempt.exam_id, attempt)
    return [
        {
            "id": exam.id,
            "title": exam.title,
            "description": exam.description,
            "time_limit_sec": exam.time_limit_sec,
            "passing_score": exam.passing_score,
            "question_count": len(exam.questions),
            "level": {"code": exam.level.code, "title": exam.level.title},
            "last_attempt": (
                {"score": latest[exam.id].score, "passed": latest[exam.id].passed}
                if exam.id in latest
                else None
            ),
        }
        for exam in exams
    ]


@router.get("/exams/{exam_id}")
def get_exam(exam_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    exam = (
        db.query(Exam)
        .options(joinedload(Exam.level), joinedload(Exam.questions))
        .filter(Exam.id == exam_id)
        .first()
    )
    if not exam:
        raise HTTPException(status_code=404, detail="Экзамен не найден")
    return {
        "id": exam.id,
        "title": exam.title,
        "description": exam.description,
        "time_limit_sec": exam.time_limit_sec,
        "passing_score": exam.passing_score,
        "level": {"code": exam.level.code, "title": exam.level.title},
        "questions": _public_questions(exam.questions),
    }


@router.post("/exams/{exam_id}/submit")
def submit_exam(
    exam_id: int,
    payload: ExamSubmitIn,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    exam = (
        db.query(Exam)
        .options(joinedload(Exam.questions))
        .filter(Exam.id == exam_id)
        .first()
    )
    if not exam:
        raise HTTPException(status_code=404, detail="Экзамен не найден")
    details = []
    correct_n = 0
    for question in exam.questions:
        given = payload.answers.get(str(question.id), "")
        ok = is_correct(given, question.answer, question.accepted)
        if ok:
            correct_n += 1
        details.append(
            {
                "id": question.id,
                "prompt": question.prompt,
                "given": given,
                "correct": ok,
                "expected": question.answer,
                "explanation": question.explanation,
            }
        )
    score = percent(correct_n, len(exam.questions))
    passed = score >= exam.passing_score
    db.add(
        ExamAttempt(
            user_id=user.id,
            exam_id=exam.id,
            score=score,
            passed=passed,
            answers=payload.answers,
        )
    )
    if passed:
        touch_user(db, user, 120)
    db.commit()
    return {"score": score, "passed": passed, "passing_score": exam.passing_score, "details": details}


@router.get("/tests/by-module/{slug}")
def get_test_by_module(slug: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    module = db.query(GrammarModule).filter(GrammarModule.slug == slug).first()
    if not module or not module.test:
        raise HTTPException(status_code=404, detail="Тест модуля не найден")
    return {"test_id": module.test.id}
