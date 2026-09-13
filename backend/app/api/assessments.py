import random

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

TEST_SAMPLE_MIN = 8
TEST_SAMPLE_MAX = 12
EXAM_SAMPLE_MIN = 12
EXAM_SAMPLE_MAX = 20


def _public_questions(items):
    return [
        {
            "id": item.id,
            "kind": item.kind,
            "prompt": item.prompt,
            "options": item.options,
            "sort_order": item.sort_order,
        }
        for item in items
    ]


def _sample_questions(questions, *, lo: int, hi: int):
    pool = list(questions)
    if not pool:
        return []
    target = min(len(pool), max(lo, min(hi, len(pool))))
    if len(pool) <= target:
        random.shuffle(pool)
        return pool
    # Mix kinds when possible
    by_kind: dict[str, list] = {}
    for q in pool:
        by_kind.setdefault(q.kind, []).append(q)
    picked = []
    kinds = list(by_kind.keys())
    random.shuffle(kinds)
    # Round-robin one from each kind first
    while len(picked) < target and any(by_kind.values()):
        progress = False
        for kind in kinds:
            bucket = by_kind.get(kind) or []
            if not bucket:
                continue
            random.shuffle(bucket)
            picked.append(bucket.pop())
            progress = True
            if len(picked) >= target:
                break
        if not progress:
            break
    if len(picked) < target:
        rest = [q for q in pool if q not in picked]
        random.shuffle(rest)
        picked.extend(rest[: target - len(picked)])
    random.shuffle(picked)
    return picked


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
    sample = _sample_questions(test.questions, lo=TEST_SAMPLE_MIN, hi=TEST_SAMPLE_MAX)
    return {
        "id": test.id,
        "title": test.title,
        "time_limit_sec": test.time_limit_sec,
        "passing_score": test.passing_score,
        "module": {"slug": test.module.slug, "title": test.module.title},
        "bank_size": len(test.questions),
        "sample_size": len(sample),
        "questions": _public_questions(sample),
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
    by_id = {str(q.id): q for q in test.questions}
    selected_ids = [qid for qid in payload.answers.keys() if qid in by_id]
    if not selected_ids:
        raise HTTPException(status_code=400, detail="Нет ответов по вопросам этого теста")
    # Cap scoring set to a reasonable attempt size (sampled subset)
    if len(selected_ids) > TEST_SAMPLE_MAX + 4:
        selected_ids = selected_ids[: TEST_SAMPLE_MAX + 4]
    details = []
    correct_n = 0
    for qid in selected_ids:
        question = by_id[qid]
        given = payload.answers.get(qid, "")
        ok = is_correct(given, question.answer, question.accepted, prompt=question.prompt)
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
    score = percent(correct_n, len(selected_ids))
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
    sample = _sample_questions(exam.questions, lo=EXAM_SAMPLE_MIN, hi=EXAM_SAMPLE_MAX)
    return {
        "id": exam.id,
        "title": exam.title,
        "description": exam.description,
        "time_limit_sec": exam.time_limit_sec,
        "passing_score": exam.passing_score,
        "level": {"code": exam.level.code, "title": exam.level.title},
        "bank_size": len(exam.questions),
        "sample_size": len(sample),
        "questions": _public_questions(sample),
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
    by_id = {str(q.id): q for q in exam.questions}
    selected_ids = [qid for qid in payload.answers.keys() if qid in by_id]
    if not selected_ids:
        raise HTTPException(status_code=400, detail="Нет ответов по вопросам этого экзамена")
    if len(selected_ids) > EXAM_SAMPLE_MAX + 6:
        selected_ids = selected_ids[: EXAM_SAMPLE_MAX + 6]
    details = []
    correct_n = 0
    for qid in selected_ids:
        question = by_id[qid]
        given = payload.answers.get(qid, "")
        ok = is_correct(given, question.answer, question.accepted, prompt=question.prompt)
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
    score = percent(correct_n, len(selected_ids))
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
