from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_admin_user
from app.core.security import hash_password
from app.models.grammar import (
    Exam,
    ExamQuestion,
    Exercise,
    GrammarLevel,
    GrammarModule,
    Lesson,
    ModuleTest,
    TestQuestion,
)
from app.models.settings import SiteSetting
from app.models.progress import ExamAttempt, ExerciseAttempt, TestAttempt
from app.models.user import User
from app.models.skills import SkillItem, SkillQuestion
from app.models.study import StudyCard, StudyDeck
from app.models.vocabulary import VocabTopic, VocabWord
from app.schemas.auth import UserUpdateIn
from app.schemas.content import (
    DonationIn,
    ExerciseIn,
    ExerciseUpdateIn,
    LessonIn,
    ModuleIn,
    ModuleUpdateIn,
    QuestionIn,
    QuestionUpdateIn,
    RegistrationSettingsIn,
    SkillItemIn,
    SkillItemUpdateIn,
    SkillQuestionIn,
    SkillQuestionUpdateIn,
    StudyCardIn,
    StudyCardUpdateIn,
    StudyDeckIn,
    StudyDeckUpdateIn,
    VocabTopicIn,
    VocabTopicUpdateIn,
    VocabWordIn,
    VocabWordUpdateIn,
)


router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/stats")
def stats(_: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    return {
        "users": db.query(func.count(User.id)).scalar() or 0,
        "students": db.query(func.count(User.id)).filter(User.role == "student").scalar() or 0,
        "modules": db.query(func.count(GrammarModule.id)).scalar() or 0,
        "exercises": db.query(func.count(Exercise.id)).scalar() or 0,
        "exams": db.query(func.count(Exam.id)).scalar() or 0,
        "vocab_words": db.query(func.count(VocabWord.id)).scalar() or 0,
        "study_cards": db.query(func.count(StudyCard.id)).scalar() or 0,
        "skill_items": db.query(func.count(SkillItem.id)).scalar() or 0,
        "practice_attempts": db.query(func.count(ExerciseAttempt.id)).scalar() or 0,
        "test_attempts": db.query(func.count(TestAttempt.id)).scalar() or 0,
        "exam_attempts": db.query(func.count(ExamAttempt.id)).scalar() or 0,
    }


@router.get("/users")
def list_users(_: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    users = db.query(User).order_by(User.created_at.desc()).all()
    return [
        {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "role": user.role,
            "is_active": user.is_active,
            "email_verified": user.email_verified,
            "xp": user.xp,
            "streak": user.streak,
            "created_at": user.created_at,
        }
        for user in users
    ]


@router.patch("/users/{user_id}")
def update_user(
    user_id: int,
    payload: UserUpdateIn,
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    if payload.name:
        user.name = payload.name.strip()
    if payload.password:
        user.hashed_password = hash_password(payload.password)
    if payload.is_active is not None:
        user.is_active = payload.is_active
    if payload.role in {"admin", "student"}:
        user.role = payload.role
    if payload.email_verified is not None:
        user.email_verified = payload.email_verified
    db.add(user)
    db.commit()
    db.refresh(user)
    return {
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "role": user.role,
        "is_active": user.is_active,
        "email_verified": user.email_verified,
        "xp": user.xp,
    }


@router.post("/users/{user_id}/activate")
def activate_user(user_id: int, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    user.email_verified = True
    user.is_active = True
    db.add(user)
    db.commit()
    db.refresh(user)
    return {
        "id": user.id,
        "email": user.email,
        "email_verified": user.email_verified,
        "is_active": user.is_active,
    }


@router.get("/levels")
def admin_levels(_: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    return [
        {"id": level.id, "code": level.code, "title": level.title}
        for level in db.query(GrammarLevel).order_by(GrammarLevel.sort_order).all()
    ]


@router.get("/modules")
def admin_modules(_: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    modules = db.query(GrammarModule).order_by(GrammarModule.level_id, GrammarModule.sort_order).all()
    return [
        {
            "id": module.id,
            "slug": module.slug,
            "title": module.title,
            "description": module.description,
            "level_id": module.level_id,
            "level_code": module.level.code,
            "sort_order": module.sort_order,
            "estimated_minutes": module.estimated_minutes,
            "sources": module.sources,
            "lesson_count": len(module.lessons),
            "exercise_count": len(module.exercises),
        }
        for module in modules
    ]


@router.post("/modules")
def create_module(payload: ModuleIn, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    if db.query(GrammarModule).filter(GrammarModule.slug == payload.slug).first():
        raise HTTPException(status_code=400, detail="Slug уже занят")
    module = GrammarModule(**payload.model_dump())
    db.add(module)
    db.commit()
    db.refresh(module)
    return {"id": module.id, "slug": module.slug}


@router.patch("/modules/{module_id}")
def update_module(
    module_id: int,
    payload: ModuleUpdateIn,
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    module = db.get(GrammarModule, module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Модуль не найден")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(module, key, value)
    db.add(module)
    db.commit()
    return {"id": module.id, "slug": module.slug, "title": module.title}


@router.delete("/modules/{module_id}")
def delete_module(module_id: int, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    module = db.get(GrammarModule, module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Модуль не найден")
    db.delete(module)
    db.commit()
    return {"ok": True}


@router.post("/modules/{module_id}/lessons")
def create_lesson(
    module_id: int,
    payload: LessonIn,
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    if not db.get(GrammarModule, module_id):
        raise HTTPException(status_code=404, detail="Модуль не найден")
    lesson = Lesson(module_id=module_id, **payload.model_dump())
    db.add(lesson)
    db.commit()
    db.refresh(lesson)
    return {"id": lesson.id}


@router.post("/modules/{module_id}/exercises")
def create_exercise(
    module_id: int,
    payload: ExerciseIn,
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    if not db.get(GrammarModule, module_id):
        raise HTTPException(status_code=404, detail="Модуль не найден")
    exercise = Exercise(module_id=module_id, **payload.model_dump())
    db.add(exercise)
    db.commit()
    db.refresh(exercise)
    return {"id": exercise.id}


@router.get("/modules/{module_id}/content")
def module_content(module_id: int, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    module = db.get(GrammarModule, module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Модуль не найден")
    return {
        "module": {"id": module.id, "title": module.title, "slug": module.slug},
        "lessons": [
            {"id": lesson.id, "title": lesson.title, "sort_order": lesson.sort_order}
            for lesson in sorted(module.lessons, key=lambda item: item.sort_order)
        ],
        "exercises": [
            {
                "id": item.id,
                "kind": item.kind,
                "prompt": item.prompt,
                "answer": item.answer,
                "options": item.options,
                "accepted": item.accepted,
                "explanation": item.explanation,
                "sort_order": item.sort_order,
            }
            for item in sorted(module.exercises, key=lambda item: item.sort_order)
        ],
        "test": (
            {
                "id": module.test.id,
                "title": module.test.title,
                "questions": [
                    {
                        "id": question.id,
                        "kind": question.kind,
                        "prompt": question.prompt,
                        "answer": question.answer,
                        "options": question.options,
                        "accepted": question.accepted,
                        "explanation": question.explanation,
                    }
                    for question in sorted(module.test.questions, key=lambda item: item.sort_order)
                ],
            }
            if module.test
            else None
        ),
    }


@router.delete("/lessons/{lesson_id}")
def delete_lesson(lesson_id: int, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    lesson = db.get(Lesson, lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail="Урок не найден")
    db.delete(lesson)
    db.commit()
    return {"ok": True}


@router.delete("/exercises/{exercise_id}")
def delete_exercise(exercise_id: int, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    exercise = db.get(Exercise, exercise_id)
    if not exercise:
        raise HTTPException(status_code=404, detail="Упражнение не найдено")
    db.delete(exercise)
    db.commit()
    return {"ok": True}


@router.patch("/exercises/{exercise_id}")
def update_exercise(
    exercise_id: int,
    payload: ExerciseUpdateIn,
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    exercise = db.get(Exercise, exercise_id)
    if not exercise:
        raise HTTPException(status_code=404, detail="Упражнение не найдено")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(exercise, key, value)
    db.add(exercise)
    db.commit()
    db.refresh(exercise)
    return {
        "id": exercise.id,
        "kind": exercise.kind,
        "prompt": exercise.prompt,
        "answer": exercise.answer,
        "options": exercise.options,
        "accepted": exercise.accepted,
        "explanation": exercise.explanation,
    }


CEFR_CODES = {"A1", "A2", "B1", "B2", "C1", "C2"}


def _norm_slug(slug: str) -> str:
    return slug.strip().lower()


def _require_level(code: str) -> str:
    level = code.strip().upper()
    if level not in CEFR_CODES:
        raise HTTPException(status_code=400, detail="Уровень должен быть A1–C2")
    return level


def _topic_slug_taken(db: Session, slug: str, exclude_id: int | None = None) -> bool:
    query = db.query(VocabTopic).filter(VocabTopic.slug == slug)
    if exclude_id is not None:
        query = query.filter(VocabTopic.id != exclude_id)
    return query.first() is not None


def _word_out(word: VocabWord) -> dict:
    return {
        "id": word.id,
        "topic_id": word.topic_id,
        "word": word.word,
        "transcription": word.transcription,
        "translation": word.translation,
        "part_of_speech": word.part_of_speech,
        "example": word.example,
        "example_translation": word.example_translation,
    }


def _topic_out(topic: VocabTopic, *, with_words: bool = False) -> dict:
    payload = {
        "id": topic.id,
        "slug": topic.slug,
        "title": topic.title,
        "description": topic.description,
        "level_code": topic.level_code,
        "sort_order": topic.sort_order,
        "word_count": len(topic.words),
    }
    if with_words:
        payload["words"] = [_word_out(word) for word in sorted(topic.words, key=lambda item: item.id)]
    return payload


@router.get("/vocab/topics")
def admin_vocab(_: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    topics = db.query(VocabTopic).order_by(VocabTopic.sort_order, VocabTopic.id).all()
    return [_topic_out(topic) for topic in topics]


@router.post("/vocab/topics")
def create_vocab_topic(payload: VocabTopicIn, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    slug = _norm_slug(payload.slug)
    if not slug:
        raise HTTPException(status_code=400, detail="Укажите slug")
    if _topic_slug_taken(db, slug):
        raise HTTPException(status_code=400, detail="Slug уже занят")
    topic = VocabTopic(
        slug=slug,
        title=payload.title.strip(),
        description=payload.description.strip(),
        level_code=_require_level(payload.level_code),
        sort_order=payload.sort_order,
    )
    db.add(topic)
    db.commit()
    db.refresh(topic)
    return _topic_out(topic)


@router.get("/vocab/topics/{topic_id}")
def admin_vocab_topic(topic_id: int, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    topic = db.get(VocabTopic, topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Тема не найдена")
    return _topic_out(topic, with_words=True)


@router.patch("/vocab/topics/{topic_id}")
def update_vocab_topic(
    topic_id: int,
    payload: VocabTopicUpdateIn,
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    topic = db.get(VocabTopic, topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Тема не найдена")
    data = payload.model_dump(exclude_unset=True)
    if "slug" in data:
        slug = _norm_slug(data["slug"] or "")
        if not slug:
            raise HTTPException(status_code=400, detail="Укажите slug")
        if _topic_slug_taken(db, slug, exclude_id=topic.id):
            raise HTTPException(status_code=400, detail="Slug уже занят")
        topic.slug = slug
    if "title" in data and data["title"] is not None:
        topic.title = data["title"].strip()
    if "description" in data and data["description"] is not None:
        topic.description = data["description"].strip()
    if "level_code" in data and data["level_code"] is not None:
        topic.level_code = _require_level(data["level_code"])
    if "sort_order" in data and data["sort_order"] is not None:
        topic.sort_order = data["sort_order"]
    db.add(topic)
    db.commit()
    db.refresh(topic)
    return _topic_out(topic, with_words=True)


@router.delete("/vocab/topics/{topic_id}")
def delete_vocab_topic(topic_id: int, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    topic = db.get(VocabTopic, topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Тема не найдена")
    db.delete(topic)
    db.commit()
    return {"ok": True}


@router.post("/vocab/words")
def create_vocab_word(payload: VocabWordIn, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    if not db.get(VocabTopic, payload.topic_id):
        raise HTTPException(status_code=404, detail="Тема не найдена")
    word = VocabWord(
        topic_id=payload.topic_id,
        word=payload.word.strip(),
        transcription=payload.transcription.strip(),
        translation=payload.translation.strip(),
        part_of_speech=payload.part_of_speech.strip() or "noun",
        example=payload.example.strip(),
        example_translation=payload.example_translation.strip(),
    )
    if not word.word or not word.translation:
        raise HTTPException(status_code=400, detail="Нужны слово и перевод")
    db.add(word)
    db.commit()
    db.refresh(word)
    return _word_out(word)


@router.patch("/vocab/words/{word_id}")
def update_vocab_word(
    word_id: int,
    payload: VocabWordUpdateIn,
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    word = db.get(VocabWord, word_id)
    if not word:
        raise HTTPException(status_code=404, detail="Слово не найдено")
    data = payload.model_dump(exclude_unset=True)
    if "topic_id" in data and data["topic_id"] is not None:
        if not db.get(VocabTopic, data["topic_id"]):
            raise HTTPException(status_code=404, detail="Тема не найдена")
        word.topic_id = data["topic_id"]
    for key in ("word", "transcription", "translation", "part_of_speech", "example", "example_translation"):
        if key in data and data[key] is not None:
            value = data[key].strip() if isinstance(data[key], str) else data[key]
            setattr(word, key, value)
    if not word.word or not word.translation:
        raise HTTPException(status_code=400, detail="Нужны слово и перевод")
    db.add(word)
    db.commit()
    db.refresh(word)
    return _word_out(word)


@router.delete("/vocab/words/{word_id}")
def delete_word(word_id: int, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    word = db.get(VocabWord, word_id)
    if not word:
        raise HTTPException(status_code=404, detail="Слово не найдено")
    db.delete(word)
    db.commit()
    return {"ok": True}


@router.get("/exams")
def admin_exams(_: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    exams = db.query(Exam).all()
    return [
        {
            "id": exam.id,
            "title": exam.title,
            "level_code": exam.level.code,
            "question_count": len(exam.questions),
            "passing_score": exam.passing_score,
        }
        for exam in exams
    ]


@router.post("/tests/{test_id}/questions")
def add_test_question(test_id: int, payload: QuestionIn, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    test = db.get(ModuleTest, test_id)
    if not test:
        raise HTTPException(status_code=404, detail="Тест не найден")
    question = TestQuestion(test_id=test.id, **payload.model_dump())
    db.add(question)
    db.commit()
    db.refresh(question)
    return {"id": question.id}


@router.delete("/test-questions/{question_id}")
def delete_test_question(question_id: int, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    question = db.get(TestQuestion, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Вопрос не найден")
    db.delete(question)
    db.commit()
    return {"ok": True}


@router.patch("/test-questions/{question_id}")
def update_test_question(
    question_id: int,
    payload: QuestionUpdateIn,
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    question = db.get(TestQuestion, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Вопрос не найден")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(question, key, value)
    db.add(question)
    db.commit()
    db.refresh(question)
    return {
        "id": question.id,
        "kind": question.kind,
        "prompt": question.prompt,
        "answer": question.answer,
        "options": question.options,
        "accepted": question.accepted,
        "explanation": question.explanation,
    }


@router.get("/exams/{exam_id}")
def admin_exam_detail(exam_id: int, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    exam = db.get(Exam, exam_id)
    if not exam:
        raise HTTPException(status_code=404, detail="Экзамен не найден")
    return {
        "id": exam.id,
        "title": exam.title,
        "level_code": exam.level.code,
        "questions": [
            {
                "id": q.id,
                "kind": q.kind,
                "prompt": q.prompt,
                "answer": q.answer,
                "options": q.options,
                "accepted": q.accepted,
                "explanation": q.explanation,
            }
            for q in sorted(exam.questions, key=lambda item: item.sort_order)
        ],
    }


@router.post("/exams/{exam_id}/questions")
def add_exam_question(exam_id: int, payload: QuestionIn, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    exam = db.get(Exam, exam_id)
    if not exam:
        raise HTTPException(status_code=404, detail="Экзамен не найден")
    question = ExamQuestion(exam_id=exam.id, **payload.model_dump())
    db.add(question)
    db.commit()
    db.refresh(question)
    return {"id": question.id}


@router.delete("/exam-questions/{question_id}")
def delete_exam_question(question_id: int, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    question = db.get(ExamQuestion, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Вопрос не найден")
    db.delete(question)
    db.commit()
    return {"ok": True}


@router.patch("/exam-questions/{question_id}")
def update_exam_question(
    question_id: int,
    payload: QuestionUpdateIn,
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    question = db.get(ExamQuestion, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Вопрос не найден")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(question, key, value)
    db.add(question)
    db.commit()
    db.refresh(question)
    return {
        "id": question.id,
        "kind": question.kind,
        "prompt": question.prompt,
        "answer": question.answer,
        "options": question.options,
        "accepted": question.accepted,
        "explanation": question.explanation,
    }


def _donation_payload(row: SiteSetting) -> dict:
    return {
        "donation_enabled": row.donation_enabled,
        "donation_title": row.donation_title,
        "donation_message": row.donation_message,
        "donation_url": row.donation_url,
        "donation_button": row.donation_button,
        "email_verification_required": getattr(row, "email_verification_required", True),
    }


@router.get("/donation")
def get_donation(_: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    row = db.get(SiteSetting, 1)
    if not row:
        row = SiteSetting(id=1)
        db.add(row)
        db.commit()
        db.refresh(row)
    return _donation_payload(row)


@router.patch("/donation")
def update_donation(payload: DonationIn, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    row = db.get(SiteSetting, 1)
    if not row:
        row = SiteSetting(id=1)
        db.add(row)
    for key, value in payload.model_dump().items():
        setattr(row, key, value.strip() if isinstance(value, str) else value)
    db.add(row)
    db.commit()
    db.refresh(row)
    return _donation_payload(row)


@router.get("/tests")
def admin_tests(_: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    tests = db.query(ModuleTest).all()
    return [
        {
            "id": test.id,
            "title": test.title,
            "module_title": test.module.title,
            "question_count": len(test.questions),
            "passing_score": test.passing_score,
        }
        for test in tests
    ]


@router.get("/registration")
def get_registration_settings(_: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    row = db.get(SiteSetting, 1)
    if not row:
        row = SiteSetting(id=1)
        db.add(row)
        db.commit()
        db.refresh(row)
    return {"email_verification_required": bool(getattr(row, "email_verification_required", True))}


@router.patch("/registration")
def update_registration_settings(
    payload: RegistrationSettingsIn,
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    row = db.get(SiteSetting, 1)
    if not row:
        row = SiteSetting(id=1)
        db.add(row)
    row.email_verification_required = payload.email_verification_required
    db.add(row)
    db.commit()
    db.refresh(row)
    return {"email_verification_required": row.email_verification_required}


def _study_card_out(card: StudyCard) -> dict:
    return {
        "id": card.id,
        "deck_id": card.deck_id,
        "primary_text": card.primary_text,
        "secondary_text": card.secondary_text,
        "tertiary_text": card.tertiary_text,
        "translation": card.translation,
        "example": card.example,
        "example_translation": card.example_translation,
        "category": card.category,
        "sort_order": card.sort_order,
    }


STUDY_KINDS = {"verbs", "idioms", "exceptions"}
SKILL_KINDS = {"reading", "listening", "dialogue"}
SKILL_QUESTION_KINDS = {"choice", "dictation", "fill_gap"}


def _require_study_kind(kind: str) -> str:
    value = kind.strip().lower()
    if value not in STUDY_KINDS:
        raise HTTPException(status_code=400, detail="Тип колоды: verbs, idioms или exceptions")
    return value


def _require_skill_kind(kind: str) -> str:
    value = kind.strip().lower()
    if value not in SKILL_KINDS:
        raise HTTPException(status_code=400, detail="Тип навыка: reading, listening или dialogue")
    return value


def _require_skill_question_kind(kind: str) -> str:
    value = kind.strip().lower()
    if value not in SKILL_QUESTION_KINDS:
        raise HTTPException(status_code=400, detail="Тип вопроса: choice, dictation или fill_gap")
    return value


def _study_deck_slug_taken(db: Session, slug: str, exclude_id: int | None = None) -> bool:
    query = db.query(StudyDeck).filter(StudyDeck.slug == slug)
    if exclude_id is not None:
        query = query.filter(StudyDeck.id != exclude_id)
    return query.first() is not None


def _skill_item_slug_taken(db: Session, slug: str, exclude_id: int | None = None) -> bool:
    query = db.query(SkillItem).filter(SkillItem.slug == slug)
    if exclude_id is not None:
        query = query.filter(SkillItem.id != exclude_id)
    return query.first() is not None


def _normalize_keywords(raw) -> list:
    if raw is None:
        return []
    if not isinstance(raw, list):
        raise HTTPException(status_code=400, detail="keywords должен быть списком")
    out = []
    for row in raw:
        if not isinstance(row, dict):
            raise HTTPException(status_code=400, detail="Каждое ключевое слово — объект {en, ru}")
        en = str(row.get("en", "")).strip()
        ru = str(row.get("ru", "")).strip()
        if en or ru:
            out.append({"en": en, "ru": ru})
    return out


def _normalize_lines(raw) -> list:
    if raw is None:
        return []
    if not isinstance(raw, list):
        raise HTTPException(status_code=400, detail="lines должен быть списком")
    out = []
    for row in raw:
        if not isinstance(row, dict):
            raise HTTPException(status_code=400, detail="Каждая реплика — объект {speaker, text, ru}")
        speaker = str(row.get("speaker", "")).strip()
        text = str(row.get("text", "")).strip()
        ru = str(row.get("ru", "")).strip()
        if speaker or text or ru:
            out.append({"speaker": speaker, "text": text, "ru": ru})
    return out


def _normalize_str_list(raw, field: str) -> list[str] | None:
    if raw is None:
        return None
    if not isinstance(raw, list):
        raise HTTPException(status_code=400, detail=f"{field} должен быть списком строк")
    values = [str(item).strip() for item in raw if str(item).strip()]
    return values or None


def _study_deck_out(deck: StudyDeck, *, with_cards: bool = False) -> dict:
    payload = {
        "id": deck.id,
        "slug": deck.slug,
        "title": deck.title,
        "description": deck.description,
        "kind": deck.kind,
        "sort_order": deck.sort_order,
        "card_count": len(deck.cards),
    }
    if with_cards:
        payload["cards"] = [_study_card_out(c) for c in sorted(deck.cards, key=lambda x: (x.sort_order, x.id))]
    return payload


def _skill_question_out(question: SkillQuestion) -> dict:
    return {
        "id": question.id,
        "item_id": question.item_id,
        "kind": question.kind,
        "prompt": question.prompt,
        "options": question.options,
        "answer": question.answer,
        "accepted": question.accepted,
        "speak": question.speak,
        "explanation": question.explanation,
        "sort_order": question.sort_order,
    }


def _skill_item_out(item: SkillItem, *, with_detail: bool = False) -> dict:
    payload = {
        "id": item.id,
        "slug": item.slug,
        "title": item.title,
        "description": item.description,
        "kind": item.kind,
        "level_code": item.level_code,
        "sort_order": item.sort_order,
        "question_count": len(item.questions),
        "keyword_count": len(item.keywords or []),
    }
    if with_detail:
        payload["body"] = item.body or ""
        payload["lines"] = item.lines or []
        payload["keywords"] = item.keywords or []
        payload["questions"] = [
            _skill_question_out(q) for q in sorted(item.questions, key=lambda x: (x.sort_order, x.id))
        ]
    return payload


@router.get("/study/decks")
def admin_study_decks(_: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    decks = db.query(StudyDeck).order_by(StudyDeck.sort_order, StudyDeck.id).all()
    return [_study_deck_out(deck) for deck in decks]


@router.post("/study/decks")
def create_study_deck(payload: StudyDeckIn, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    slug = _norm_slug(payload.slug)
    if not slug:
        raise HTTPException(status_code=400, detail="Укажите slug")
    if _study_deck_slug_taken(db, slug):
        raise HTTPException(status_code=400, detail="Slug уже занят")
    deck = StudyDeck(
        slug=slug,
        title=payload.title.strip(),
        description=payload.description.strip(),
        kind=_require_study_kind(payload.kind),
        sort_order=payload.sort_order,
    )
    db.add(deck)
    db.commit()
    db.refresh(deck)
    return _study_deck_out(deck)


@router.get("/study/decks/{deck_id}")
def admin_study_deck(deck_id: int, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    deck = db.get(StudyDeck, deck_id)
    if not deck:
        raise HTTPException(status_code=404, detail="Колода не найдена")
    return _study_deck_out(deck, with_cards=True)


@router.patch("/study/decks/{deck_id}")
def update_study_deck(
    deck_id: int,
    payload: StudyDeckUpdateIn,
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    deck = db.get(StudyDeck, deck_id)
    if not deck:
        raise HTTPException(status_code=404, detail="Колода не найдена")
    data = payload.model_dump(exclude_unset=True)
    if "slug" in data:
        slug = _norm_slug(data["slug"] or "")
        if not slug:
            raise HTTPException(status_code=400, detail="Укажите slug")
        if _study_deck_slug_taken(db, slug, exclude_id=deck.id):
            raise HTTPException(status_code=400, detail="Slug уже занят")
        deck.slug = slug
    if "title" in data and data["title"] is not None:
        deck.title = data["title"].strip()
    if "description" in data and data["description"] is not None:
        deck.description = data["description"].strip()
    if "kind" in data and data["kind"] is not None:
        deck.kind = _require_study_kind(data["kind"])
    if "sort_order" in data and data["sort_order"] is not None:
        deck.sort_order = data["sort_order"]
    db.add(deck)
    db.commit()
    db.refresh(deck)
    return _study_deck_out(deck, with_cards=True)


@router.delete("/study/decks/{deck_id}")
def delete_study_deck(deck_id: int, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    deck = db.get(StudyDeck, deck_id)
    if not deck:
        raise HTTPException(status_code=404, detail="Колода не найдена")
    db.delete(deck)
    db.commit()
    return {"ok": True}


@router.post("/study/cards")
def create_study_card(payload: StudyCardIn, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    if not db.get(StudyDeck, payload.deck_id):
        raise HTTPException(status_code=404, detail="Колода не найдена")
    data = payload.model_dump()
    for key in ("primary_text", "secondary_text", "tertiary_text", "translation", "example", "example_translation", "category"):
        if isinstance(data.get(key), str):
            data[key] = data[key].strip()
    if not data["primary_text"] or not data["translation"]:
        raise HTTPException(status_code=400, detail="Нужны основной текст и перевод")
    card = StudyCard(**data)
    db.add(card)
    db.commit()
    db.refresh(card)
    return _study_card_out(card)


@router.patch("/study/cards/{card_id}")
def update_study_card(
    card_id: int,
    payload: StudyCardUpdateIn,
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    card = db.get(StudyCard, card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Карточка не найдена")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(card, key, value.strip() if isinstance(value, str) else value)
    if not card.primary_text or not card.translation:
        raise HTTPException(status_code=400, detail="Нужны основной текст и перевод")
    db.add(card)
    db.commit()
    db.refresh(card)
    return _study_card_out(card)


@router.delete("/study/cards/{card_id}")
def delete_study_card(card_id: int, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    card = db.get(StudyCard, card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Карточка не найдена")
    db.delete(card)
    db.commit()
    return {"ok": True}


@router.get("/skills")
def admin_skills(_: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    items = db.query(SkillItem).order_by(SkillItem.kind, SkillItem.sort_order, SkillItem.id).all()
    return [_skill_item_out(item) for item in items]


@router.post("/skills")
def create_skill_item(payload: SkillItemIn, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    slug = _norm_slug(payload.slug)
    if not slug:
        raise HTTPException(status_code=400, detail="Укажите slug")
    if _skill_item_slug_taken(db, slug):
        raise HTTPException(status_code=400, detail="Slug уже занят")
    item = SkillItem(
        slug=slug,
        title=payload.title.strip(),
        description=payload.description.strip(),
        kind=_require_skill_kind(payload.kind),
        level_code=_require_level(payload.level_code),
        body=payload.body.strip() if payload.body else "",
        lines=_normalize_lines(payload.lines),
        keywords=_normalize_keywords(payload.keywords),
        sort_order=payload.sort_order,
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return _skill_item_out(item, with_detail=True)


@router.post("/skills/questions")
def create_skill_question(
    payload: SkillQuestionIn,
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    if not db.get(SkillItem, payload.item_id):
        raise HTTPException(status_code=404, detail="Материал не найден")
    kind = _require_skill_question_kind(payload.kind)
    prompt = payload.prompt.strip()
    answer = payload.answer.strip()
    if not prompt or not answer:
        raise HTTPException(status_code=400, detail="Нужны вопрос и ответ")
    question = SkillQuestion(
        item_id=payload.item_id,
        kind=kind,
        prompt=prompt,
        options=_normalize_str_list(payload.options, "options"),
        answer=answer,
        accepted=_normalize_str_list(payload.accepted, "accepted"),
        speak=(payload.speak or "").strip(),
        explanation=(payload.explanation or "").strip(),
        sort_order=payload.sort_order,
    )
    db.add(question)
    db.commit()
    db.refresh(question)
    return _skill_question_out(question)


@router.patch("/skills/questions/{question_id}")
def update_skill_question(
    question_id: int,
    payload: SkillQuestionUpdateIn,
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    question = db.get(SkillQuestion, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Вопрос не найден")
    data = payload.model_dump(exclude_unset=True)
    if "kind" in data and data["kind"] is not None:
        question.kind = _require_skill_question_kind(data["kind"])
    if "prompt" in data and data["prompt"] is not None:
        question.prompt = data["prompt"].strip()
    if "answer" in data and data["answer"] is not None:
        question.answer = data["answer"].strip()
    if "speak" in data and data["speak"] is not None:
        question.speak = data["speak"].strip()
    if "explanation" in data and data["explanation"] is not None:
        question.explanation = data["explanation"].strip()
    if "options" in data:
        question.options = _normalize_str_list(data["options"], "options")
    if "accepted" in data:
        question.accepted = _normalize_str_list(data["accepted"], "accepted")
    if "sort_order" in data and data["sort_order"] is not None:
        question.sort_order = data["sort_order"]
    if not question.prompt or not question.answer:
        raise HTTPException(status_code=400, detail="Нужны вопрос и ответ")
    db.add(question)
    db.commit()
    db.refresh(question)
    return _skill_question_out(question)


@router.delete("/skills/questions/{question_id}")
def delete_skill_question(question_id: int, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    question = db.get(SkillQuestion, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Вопрос не найден")
    db.delete(question)
    db.commit()
    return {"ok": True}


@router.get("/skills/{item_id}")
def admin_skill_item(item_id: int, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    item = db.get(SkillItem, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Материал не найден")
    return _skill_item_out(item, with_detail=True)


@router.patch("/skills/{item_id}")
def update_skill_item(
    item_id: int,
    payload: SkillItemUpdateIn,
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
):
    item = db.get(SkillItem, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Материал не найден")
    data = payload.model_dump(exclude_unset=True)
    if "slug" in data:
        slug = _norm_slug(data["slug"] or "")
        if not slug:
            raise HTTPException(status_code=400, detail="Укажите slug")
        if _skill_item_slug_taken(db, slug, exclude_id=item.id):
            raise HTTPException(status_code=400, detail="Slug уже занят")
        item.slug = slug
    if "title" in data and data["title"] is not None:
        item.title = data["title"].strip()
    if "description" in data and data["description"] is not None:
        item.description = data["description"].strip()
    if "kind" in data and data["kind"] is not None:
        item.kind = _require_skill_kind(data["kind"])
    if "level_code" in data and data["level_code"] is not None:
        item.level_code = _require_level(data["level_code"])
    if "body" in data and data["body"] is not None:
        item.body = data["body"].strip()
    if "lines" in data:
        item.lines = _normalize_lines(data["lines"])
    if "keywords" in data:
        item.keywords = _normalize_keywords(data["keywords"])
    if "sort_order" in data and data["sort_order"] is not None:
        item.sort_order = data["sort_order"]
    db.add(item)
    db.commit()
    db.refresh(item)
    return _skill_item_out(item, with_detail=True)


@router.delete("/skills/{item_id}")
def delete_skill_item(item_id: int, _: User = Depends(get_admin_user), db: Session = Depends(get_db)):
    item = db.get(SkillItem, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Материал не найден")
    db.delete(item)
    db.commit()
    return {"ok": True}
