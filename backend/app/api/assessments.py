import random
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.orm.attributes import flag_modified

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.grammar import Exam, GrammarModule, ModuleTest
from app.models.progress import ExamAttempt, TestAttempt
from app.models.user import User
from app.schemas.content import AttemptAnswersIn, AttemptSubmitIn
from app.services.scoring import (
    get_or_create_progress,
    is_correct,
    missing_required_marker_hint,
    percent,
    refresh_module_status,
    touch_user,
)

router = APIRouter(tags=["assessments"])

TEST_SAMPLE_MIN = 8
TEST_SAMPLE_MAX = 12
EXAM_SAMPLE_MIN = 12
EXAM_SAMPLE_MAX = 20
STATUS_IN_PROGRESS = "in_progress"
STATUS_SUBMITTED = "submitted"


def _public_options(item):
    if getattr(item, "kind", None) == "match":
        from app.services.match_format import public_match_options

        sides = public_match_options(item.options, item.answer)
        if sides:
            return sides
    return item.options


def _public_questions(items):
    return [
        {
            "id": item.id,
            "kind": item.kind,
            "prompt": item.prompt,
            "options": _public_options(item),
            "sort_order": item.sort_order,
        }
        for item in items
    ]


def _sample_questions(questions, *, lo: int, hi: int):
    """Sample a balanced attempt; never return two items with the same prompt."""
    pool = []
    seen_prompts: set[str] = set()
    for q in questions:
        prompt = (q.prompt or "").strip()
        if prompt and prompt in seen_prompts:
            continue
        if prompt:
            seen_prompts.add(prompt)
        pool.append(q)
    if not pool:
        return []
    target = min(len(pool), max(lo, min(hi, len(pool))))
    if len(pool) <= target:
        random.shuffle(pool)
        return pool
    by_kind: dict[str, list] = {}
    for q in pool:
        by_kind.setdefault(q.kind, []).append(q)
    picked = []
    kinds = list(by_kind.keys())
    random.shuffle(kinds)
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


def _planned_sample_size(n: int, *, lo: int, hi: int) -> int:
    if n <= 0:
        return 0
    return min(n, max(lo, min(hi, n)))


def _detail_explanation(question, given: str, ok: bool) -> str | None:
    explanation = question.explanation
    if ok or question.kind != "transform":
        return explanation
    hint = missing_required_marker_hint(given, question.answer, question.prompt)
    if not hint:
        return explanation
    return f"{hint} {explanation}" if explanation else hint


def _aware(dt: datetime | None) -> datetime | None:
    if dt is None:
        return None
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _remaining_sec(ends_at: datetime | None) -> int | None:
    ends = _aware(ends_at)
    if ends is None:
        return None
    return max(0, int((ends - _now()).total_seconds()))


def _ordered_questions(bank, question_ids: list | None):
    by_id = {q.id: q for q in bank}
    ids = question_ids or []
    return [by_id[int(qid)] for qid in ids if int(qid) in by_id]


def _score_details(questions, answers: dict) -> tuple[int, list]:
    details = []
    correct_n = 0
    for question in questions:
        qid = str(question.id)
        given = (answers or {}).get(qid, "")
        ok = is_correct(
            given,
            question.answer,
            question.accepted,
            prompt=question.prompt,
            kind=question.kind,
        )
        if ok:
            correct_n += 1
        details.append(
            {
                "id": question.id,
                "prompt": question.prompt,
                "kind": question.kind,
                "given": given,
                "correct": ok,
                "expected": question.answer,
                "explanation": _detail_explanation(question, given, ok),
            }
        )
    score = percent(correct_n, len(questions))
    return score, details


def _history_item(attempt) -> dict:
    return {
        "id": attempt.id,
        "score": attempt.score,
        "passed": attempt.passed,
        "status": attempt.status,
        "started_at": attempt.started_at or attempt.created_at,
        "created_at": attempt.created_at,
        "ends_at": attempt.ends_at,
    }


def _attempt_public(attempt, *, questions=None, include_details: bool = False) -> dict:
    payload = {
        "id": attempt.id,
        "status": attempt.status,
        "question_ids": attempt.question_ids or [],
        "answers": attempt.answers or {},
        "score": attempt.score,
        "passed": attempt.passed,
        "started_at": attempt.started_at or attempt.created_at,
        "ends_at": attempt.ends_at,
        "created_at": attempt.created_at,
        "remaining_sec": _remaining_sec(attempt.ends_at) if attempt.status == STATUS_IN_PROGRESS else None,
    }
    if questions is not None:
        payload["questions"] = _public_questions(questions)
    if include_details:
        payload["details"] = attempt.details
    return payload


def _active_test_attempt(db: Session, user_id: int, test_id: int) -> TestAttempt | None:
    return (
        db.query(TestAttempt)
        .filter(
            TestAttempt.user_id == user_id,
            TestAttempt.test_id == test_id,
            TestAttempt.status == STATUS_IN_PROGRESS,
        )
        .order_by(TestAttempt.started_at.desc().nullslast(), TestAttempt.id.desc())
        .first()
    )


def _active_exam_attempt(db: Session, user_id: int, exam_id: int) -> ExamAttempt | None:
    return (
        db.query(ExamAttempt)
        .filter(
            ExamAttempt.user_id == user_id,
            ExamAttempt.exam_id == exam_id,
            ExamAttempt.status == STATUS_IN_PROGRESS,
        )
        .order_by(ExamAttempt.started_at.desc().nullslast(), ExamAttempt.id.desc())
        .first()
    )


def _finalize_test_attempt(db: Session, attempt: TestAttempt, test: ModuleTest, answers: dict | None = None):
    if attempt.status == STATUS_SUBMITTED:
        return attempt
    if answers is not None:
        attempt.answers = {**(attempt.answers or {}), **answers}
        flag_modified(attempt, "answers")
    questions = _ordered_questions(test.questions, attempt.question_ids)
    score, details = _score_details(questions, attempt.answers or {})
    passed = score >= test.passing_score
    attempt.score = score
    attempt.passed = passed
    attempt.details = details
    attempt.status = STATUS_SUBMITTED
    flag_modified(attempt, "details")
    progress = get_or_create_progress(db, attempt.user_id, test.module_id)
    if progress.test_score is None or score > progress.test_score:
        progress.test_score = score
    refresh_module_status(progress)
    if passed:
        user = db.get(User, attempt.user_id)
        if user:
            touch_user(db, user, 40)
    return attempt


def _finalize_exam_attempt(db: Session, attempt: ExamAttempt, exam: Exam, answers: dict | None = None):
    if attempt.status == STATUS_SUBMITTED:
        return attempt
    if answers is not None:
        attempt.answers = {**(attempt.answers or {}), **answers}
        flag_modified(attempt, "answers")
    questions = _ordered_questions(exam.questions, attempt.question_ids)
    score, details = _score_details(questions, attempt.answers or {})
    passed = score >= exam.passing_score
    attempt.score = score
    attempt.passed = passed
    attempt.details = details
    attempt.status = STATUS_SUBMITTED
    flag_modified(attempt, "details")
    if passed:
        user = db.get(User, attempt.user_id)
        if user:
            touch_user(db, user, 120)
    return attempt


def _maybe_expire_test(db: Session, attempt: TestAttempt | None, test: ModuleTest) -> TestAttempt | None:
    if not attempt or attempt.status != STATUS_IN_PROGRESS:
        return attempt
    ends = _aware(attempt.ends_at)
    if ends is not None and ends <= _now():
        _finalize_test_attempt(db, attempt, test)
        db.commit()
        db.refresh(attempt)
    return attempt


def _maybe_expire_exam(db: Session, attempt: ExamAttempt | None, exam: Exam) -> ExamAttempt | None:
    if not attempt or attempt.status != STATUS_IN_PROGRESS:
        return attempt
    ends = _aware(attempt.ends_at)
    if ends is not None and ends <= _now():
        _finalize_exam_attempt(db, attempt, exam)
        db.commit()
        db.refresh(attempt)
    return attempt


def _ensure_attempt_owner(attempt, user: User):
    if not attempt or attempt.user_id != user.id:
        raise HTTPException(status_code=404, detail="Попытка не найдена")


@router.get("/tests/by-module/{slug}")
def get_test_by_module(slug: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    module = db.query(GrammarModule).filter(GrammarModule.slug == slug).first()
    if not module or not module.test:
        raise HTTPException(status_code=404, detail="Тест модуля не найден")
    return {"test_id": module.test.id}


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
    active = _maybe_expire_test(db, _active_test_attempt(db, user.id, test.id), test)
    if active and active.status != STATUS_IN_PROGRESS:
        active = None
    history = (
        db.query(TestAttempt)
        .filter(
            TestAttempt.user_id == user.id,
            TestAttempt.test_id == test.id,
            TestAttempt.status == STATUS_SUBMITTED,
        )
        .order_by(TestAttempt.created_at.desc())
        .limit(20)
        .all()
    )
    last = history[0] if history else None
    bank_size = len(test.questions)
    return {
        "id": test.id,
        "title": test.title,
        "time_limit_sec": test.time_limit_sec,
        "passing_score": test.passing_score,
        "module": {"slug": test.module.slug, "title": test.module.title},
        "bank_size": bank_size,
        "sample_size": _planned_sample_size(bank_size, lo=TEST_SAMPLE_MIN, hi=TEST_SAMPLE_MAX),
        "active_attempt": (
            {
                "id": active.id,
                "started_at": active.started_at or active.created_at,
                "ends_at": active.ends_at,
                "remaining_sec": _remaining_sec(active.ends_at),
            }
            if active
            else None
        ),
        "history": [_history_item(h) for h in history],
        "last_attempt": {"score": last.score, "passed": last.passed} if last else None,
    }


@router.post("/tests/{test_id}/attempts")
def start_test_attempt(test_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    test = (
        db.query(ModuleTest)
        .options(joinedload(ModuleTest.questions))
        .filter(ModuleTest.id == test_id)
        .first()
    )
    if not test:
        raise HTTPException(status_code=404, detail="Тест не найден")
    active = _maybe_expire_test(db, _active_test_attempt(db, user.id, test.id), test)
    if active and active.status == STATUS_IN_PROGRESS:
        questions = _ordered_questions(test.questions, active.question_ids)
        return _attempt_public(active, questions=questions)

    sample = _sample_questions(test.questions, lo=TEST_SAMPLE_MIN, hi=TEST_SAMPLE_MAX)
    if not sample:
        raise HTTPException(status_code=400, detail="В тесте нет вопросов")
    now = _now()
    ends = now + timedelta(seconds=test.time_limit_sec) if test.time_limit_sec else None
    attempt = TestAttempt(
        user_id=user.id,
        test_id=test.id,
        status=STATUS_IN_PROGRESS,
        question_ids=[q.id for q in sample],
        answers={},
        details=None,
        score=None,
        passed=None,
        started_at=now,
        ends_at=ends,
    )
    db.add(attempt)
    db.commit()
    db.refresh(attempt)
    return _attempt_public(attempt, questions=sample)


@router.get("/tests/{test_id}/attempts/active")
def get_active_test_attempt(test_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    test = (
        db.query(ModuleTest)
        .options(joinedload(ModuleTest.questions))
        .filter(ModuleTest.id == test_id)
        .first()
    )
    if not test:
        raise HTTPException(status_code=404, detail="Тест не найден")
    active = _maybe_expire_test(db, _active_test_attempt(db, user.id, test.id), test)
    if not active or active.status != STATUS_IN_PROGRESS:
        raise HTTPException(status_code=404, detail="Нет активной попытки")
    questions = _ordered_questions(test.questions, active.question_ids)
    return _attempt_public(active, questions=questions)


@router.get("/tests/{test_id}/attempts/{attempt_id}")
def get_test_attempt(
    test_id: int,
    attempt_id: int,
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
    attempt = db.get(TestAttempt, attempt_id)
    _ensure_attempt_owner(attempt, user)
    if attempt.test_id != test.id:
        raise HTTPException(status_code=404, detail="Попытка не найдена")
    attempt = _maybe_expire_test(db, attempt, test)
    questions = _ordered_questions(test.questions, attempt.question_ids)
    if attempt.status == STATUS_IN_PROGRESS:
        return _attempt_public(attempt, questions=questions)
    if not attempt.details and questions:
        _, details = _score_details(questions, attempt.answers or {})
        attempt.details = details
        db.commit()
    return {
        **_attempt_public(attempt, include_details=True),
        "passing_score": test.passing_score,
        "title": test.title,
    }


@router.patch("/tests/attempts/{attempt_id}")
def save_test_answers(
    attempt_id: int,
    payload: AttemptAnswersIn,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    attempt = db.get(TestAttempt, attempt_id)
    _ensure_attempt_owner(attempt, user)
    test = db.query(ModuleTest).options(joinedload(ModuleTest.questions)).filter(ModuleTest.id == attempt.test_id).first()
    if not test:
        raise HTTPException(status_code=404, detail="Тест не найден")
    attempt = _maybe_expire_test(db, attempt, test)
    if attempt.status != STATUS_IN_PROGRESS:
        raise HTTPException(status_code=400, detail="Попытка уже завершена")
    allowed = {str(qid) for qid in (attempt.question_ids or [])}
    merged = dict(attempt.answers or {})
    for key, value in payload.answers.items():
        if key in allowed:
            merged[key] = value
    attempt.answers = merged
    flag_modified(attempt, "answers")
    db.commit()
    db.refresh(attempt)
    return {
        "id": attempt.id,
        "status": attempt.status,
        "answers": attempt.answers,
        "remaining_sec": _remaining_sec(attempt.ends_at),
        "ends_at": attempt.ends_at,
    }


@router.post("/tests/attempts/{attempt_id}/submit")
def submit_test_attempt(
    attempt_id: int,
    payload: AttemptSubmitIn,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    attempt = db.get(TestAttempt, attempt_id)
    _ensure_attempt_owner(attempt, user)
    test = db.query(ModuleTest).options(joinedload(ModuleTest.questions)).filter(ModuleTest.id == attempt.test_id).first()
    if not test:
        raise HTTPException(status_code=404, detail="Тест не найден")
    if attempt.status == STATUS_SUBMITTED:
        return {
            "attempt_id": attempt.id,
            "score": attempt.score,
            "passed": attempt.passed,
            "passing_score": test.passing_score,
            "details": attempt.details or [],
        }
    _finalize_test_attempt(db, attempt, test, payload.answers)
    db.commit()
    db.refresh(attempt)
    return {
        "attempt_id": attempt.id,
        "score": attempt.score,
        "passed": attempt.passed,
        "passing_score": test.passing_score,
        "details": attempt.details or [],
    }


@router.get("/exams")
def list_exams(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    exams = db.query(Exam).options(joinedload(Exam.level)).order_by(Exam.id).all()
    attempts = (
        db.query(ExamAttempt)
        .filter(ExamAttempt.user_id == user.id, ExamAttempt.status == STATUS_SUBMITTED)
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
            "question_count": _planned_sample_size(
                len(exam.questions), lo=EXAM_SAMPLE_MIN, hi=EXAM_SAMPLE_MAX
            ),
            "bank_size": len(exam.questions),
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
    active = _maybe_expire_exam(db, _active_exam_attempt(db, user.id, exam.id), exam)
    if active and active.status != STATUS_IN_PROGRESS:
        active = None
    history = (
        db.query(ExamAttempt)
        .filter(
            ExamAttempt.user_id == user.id,
            ExamAttempt.exam_id == exam.id,
            ExamAttempt.status == STATUS_SUBMITTED,
        )
        .order_by(ExamAttempt.created_at.desc())
        .limit(20)
        .all()
    )
    last = history[0] if history else None
    bank_size = len(exam.questions)
    return {
        "id": exam.id,
        "title": exam.title,
        "description": exam.description,
        "time_limit_sec": exam.time_limit_sec,
        "passing_score": exam.passing_score,
        "level": {"code": exam.level.code, "title": exam.level.title},
        "bank_size": bank_size,
        "sample_size": _planned_sample_size(bank_size, lo=EXAM_SAMPLE_MIN, hi=EXAM_SAMPLE_MAX),
        "active_attempt": (
            {
                "id": active.id,
                "started_at": active.started_at or active.created_at,
                "ends_at": active.ends_at,
                "remaining_sec": _remaining_sec(active.ends_at),
            }
            if active
            else None
        ),
        "history": [_history_item(h) for h in history],
        "last_attempt": {"score": last.score, "passed": last.passed} if last else None,
    }


@router.post("/exams/{exam_id}/attempts")
def start_exam_attempt(exam_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    exam = (
        db.query(Exam)
        .options(joinedload(Exam.questions))
        .filter(Exam.id == exam_id)
        .first()
    )
    if not exam:
        raise HTTPException(status_code=404, detail="Экзамен не найден")
    active = _maybe_expire_exam(db, _active_exam_attempt(db, user.id, exam.id), exam)
    if active and active.status == STATUS_IN_PROGRESS:
        questions = _ordered_questions(exam.questions, active.question_ids)
        return _attempt_public(active, questions=questions)

    sample = _sample_questions(exam.questions, lo=EXAM_SAMPLE_MIN, hi=EXAM_SAMPLE_MAX)
    if not sample:
        raise HTTPException(status_code=400, detail="В экзамене нет вопросов")
    now = _now()
    ends = now + timedelta(seconds=exam.time_limit_sec) if exam.time_limit_sec else None
    attempt = ExamAttempt(
        user_id=user.id,
        exam_id=exam.id,
        status=STATUS_IN_PROGRESS,
        question_ids=[q.id for q in sample],
        answers={},
        details=None,
        score=None,
        passed=None,
        started_at=now,
        ends_at=ends,
    )
    db.add(attempt)
    db.commit()
    db.refresh(attempt)
    return _attempt_public(attempt, questions=sample)


@router.get("/exams/{exam_id}/attempts/active")
def get_active_exam_attempt(exam_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    exam = (
        db.query(Exam)
        .options(joinedload(Exam.questions))
        .filter(Exam.id == exam_id)
        .first()
    )
    if not exam:
        raise HTTPException(status_code=404, detail="Экзамен не найден")
    active = _maybe_expire_exam(db, _active_exam_attempt(db, user.id, exam.id), exam)
    if not active or active.status != STATUS_IN_PROGRESS:
        raise HTTPException(status_code=404, detail="Нет активной попытки")
    questions = _ordered_questions(exam.questions, active.question_ids)
    return _attempt_public(active, questions=questions)


@router.get("/exams/{exam_id}/attempts/{attempt_id}")
def get_exam_attempt(
    exam_id: int,
    attempt_id: int,
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
    attempt = db.get(ExamAttempt, attempt_id)
    _ensure_attempt_owner(attempt, user)
    if attempt.exam_id != exam.id:
        raise HTTPException(status_code=404, detail="Попытка не найдена")
    attempt = _maybe_expire_exam(db, attempt, exam)
    questions = _ordered_questions(exam.questions, attempt.question_ids)
    if attempt.status == STATUS_IN_PROGRESS:
        return _attempt_public(attempt, questions=questions)
    if not attempt.details and questions:
        _, details = _score_details(questions, attempt.answers or {})
        attempt.details = details
        db.commit()
    return {
        **_attempt_public(attempt, include_details=True),
        "passing_score": exam.passing_score,
        "title": exam.title,
    }


@router.patch("/exams/attempts/{attempt_id}")
def save_exam_answers(
    attempt_id: int,
    payload: AttemptAnswersIn,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    attempt = db.get(ExamAttempt, attempt_id)
    _ensure_attempt_owner(attempt, user)
    exam = db.query(Exam).options(joinedload(Exam.questions)).filter(Exam.id == attempt.exam_id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="Экзамен не найден")
    attempt = _maybe_expire_exam(db, attempt, exam)
    if attempt.status != STATUS_IN_PROGRESS:
        raise HTTPException(status_code=400, detail="Попытка уже завершена")
    allowed = {str(qid) for qid in (attempt.question_ids or [])}
    merged = dict(attempt.answers or {})
    for key, value in payload.answers.items():
        if key in allowed:
            merged[key] = value
    attempt.answers = merged
    flag_modified(attempt, "answers")
    db.commit()
    db.refresh(attempt)
    return {
        "id": attempt.id,
        "status": attempt.status,
        "answers": attempt.answers,
        "remaining_sec": _remaining_sec(attempt.ends_at),
        "ends_at": attempt.ends_at,
    }


@router.post("/exams/attempts/{attempt_id}/submit")
def submit_exam_attempt(
    attempt_id: int,
    payload: AttemptSubmitIn,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    attempt = db.get(ExamAttempt, attempt_id)
    _ensure_attempt_owner(attempt, user)
    exam = db.query(Exam).options(joinedload(Exam.questions)).filter(Exam.id == attempt.exam_id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="Экзамен не найден")
    if attempt.status == STATUS_SUBMITTED:
        return {
            "attempt_id": attempt.id,
            "score": attempt.score,
            "passed": attempt.passed,
            "passing_score": exam.passing_score,
            "details": attempt.details or [],
        }
    _finalize_exam_attempt(db, attempt, exam, payload.answers)
    db.commit()
    db.refresh(attempt)
    return {
        "attempt_id": attempt.id,
        "score": attempt.score,
        "passed": attempt.passed,
        "passing_score": exam.passing_score,
        "details": attempt.details or [],
    }
