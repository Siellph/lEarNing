from sqlalchemy import inspect, text

from app.core.config import settings
from app.core.security import hash_password
from app.models.grammar import Exam, ExamQuestion, Exercise, GrammarModule, ModuleTest, TestQuestion
from app.models.settings import SiteSetting
from app.models.user import User
from app.models.vocabulary import VocabTopic, VocabWord
from app.seed.extra_exams import EXTRA_EXAMS
from app.seed.extra_vocab import EXTRA_WORDS_BY_SLUG, NEW_TOPICS
from app.seed.more_vocab import MORE_TOPICS, MORE_WORDS_BY_SLUG
from app.seed.plus_vocab import PLUS_TOPICS, PLUS_WORDS_BY_SLUG


def _fields(item) -> dict:
    if isinstance(item, Exercise):
        return {
            "kind": item.kind,
            "prompt": item.prompt,
            "options": item.options,
            "answer": item.answer,
            "accepted": item.accepted,
            "explanation": item.explanation,
        }
    return {
        "kind": item["kind"],
        "prompt": item["prompt"],
        "options": item.get("options"),
        "answer": item["answer"],
        "accepted": item.get("accepted"),
        "explanation": item["explanation"],
    }


def expand_module_tests(db, minimum: int = 12) -> int:
    added = 0
    tests = db.query(ModuleTest).all()
    for test in tests:
        prompts = {question.prompt for question in test.questions}
        order = max((question.sort_order for question in test.questions), default=0)
        if len(test.questions) < minimum:
            extras = (
                db.query(Exercise)
                .filter(Exercise.module_id == test.module_id)
                .order_by(Exercise.sort_order)
                .all()
            )
            for exercise in extras:
                if exercise.prompt in prompts:
                    continue
                order += 1
                db.add(TestQuestion(test_id=test.id, sort_order=order, **_fields(exercise)))
                prompts.add(exercise.prompt)
                added += 1
                if len(prompts) >= minimum:
                    break
        if test.time_limit_sec < 900:
            test.time_limit_sec = 900
    return added


def expand_exams(db) -> int:
    added = 0
    exams = db.query(Exam).all()
    for exam in exams:
        extras = EXTRA_EXAMS.get(exam.level.code, [])
        prompts = {question.prompt for question in exam.questions}
        order = max((question.sort_order for question in exam.questions), default=0)
        for item in extras:
            if item["prompt"] in prompts:
                continue
            order += 1
            db.add(ExamQuestion(exam_id=exam.id, sort_order=order, **_fields(item)))
            prompts.add(item["prompt"])
            added += 1
        if exam.time_limit_sec < 1800:
            exam.time_limit_sec = 1800
    return added


DONATION_MESSAGE = (
    "Если lEarNing помогает учить EN, можно оставить чаевые — это поддерживает развитие курса."
)


def ensure_site_settings(db) -> None:
    row = db.get(SiteSetting, 1)
    if row is None:
        db.add(SiteSetting(id=1, donation_message=DONATION_MESSAGE))
        return
    if "Lumina" in (row.donation_message or ""):
        row.donation_message = DONATION_MESSAGE


def ensure_email_verified_column(engine) -> None:
    inspector = inspect(engine)
    if "users" not in inspector.get_table_names():
        return
    columns = {column["name"] for column in inspector.get_columns("users")}
    if "email_verified" in columns:
        return
    with engine.begin() as conn:
        conn.execute(text("ALTER TABLE users ADD COLUMN email_verified BOOLEAN NOT NULL DEFAULT TRUE"))


# Leftover fixture accounts only. Never recreate. Do not add real people here.
PROTECTED_EMAILS = frozenset({"i@vgordin.ru"})
LEGACY_DEMO_EMAILS = (
    "admin@lumina.local",
    "demo@lumina.local",
    "test@lumina.local",
    "student@lumina.local",
    "user@lumina.local",
    "demo@example.com",
    "test@example.com",
    "terms-ok-2026@example.com",
    "verify-test-963682243@example.com",
    "verify-final-912@example.com",
    "vocab-batch-912@example.com",
)
LEGACY_TEST_PREFIXES = (
    "verify-test-",
    "verify-final-",
    "vocab-batch-",
    "terms-ok-",
)


def _is_legacy_test_email(email: str) -> bool:
    lowered = email.strip().lower()
    if lowered in LEGACY_DEMO_EMAILS or lowered.endswith("@lumina.local"):
        return True
    local = lowered.split("@", 1)[0]
    return any(local.startswith(prefix) for prefix in LEGACY_TEST_PREFIXES)


def remove_legacy_demo_accounts(db) -> int:
    """Delete leftover demo/test users. Do not recreate them or touch real accounts."""
    env_admin = (settings.ADMIN_EMAIL or "").strip().lower()
    removed = 0
    for user in db.query(User).all():
        email = (user.email or "").strip().lower()
        if not email or email in PROTECTED_EMAILS or (env_admin and email == env_admin):
            continue
        if not _is_legacy_test_email(email):
            continue
        db.delete(user)
        removed += 1
    return removed


def ensure_admin_from_env(db) -> bool:
    email = (settings.ADMIN_EMAIL or "").strip().lower()
    password = settings.ADMIN_PASSWORD or ""
    name = (settings.ADMIN_NAME or "").strip() or "Администратор"
    if not email or not password:
        return False
    existing = db.query(User).filter(User.email == email).first()
    if existing is not None:
        return False
    db.add(
        User(
            email=email,
            name=name,
            hashed_password=hash_password(password),
            role="admin",
            email_verified=True,
            is_active=True,
        )
    )
    return True


def expand_vocabulary(db) -> int:
    added = 0
    topics = {topic.slug: topic for topic in db.query(VocabTopic).all()}
    max_order = max((topic.sort_order for topic in topics.values()), default=0)

    extra_by_slug: dict[str, list] = {}
    for mapping in (EXTRA_WORDS_BY_SLUG, MORE_WORDS_BY_SLUG, PLUS_WORDS_BY_SLUG):
        for slug, words in mapping.items():
            extra_by_slug.setdefault(slug, []).extend(words)

    for slug, words in extra_by_slug.items():
        topic = topics.get(slug)
        if topic is None:
            continue
        existing = {word.word.lower() for word in topic.words}
        for item in words:
            if item["word"].lower() in existing:
                continue
            db.add(VocabWord(topic_id=topic.id, **item))
            existing.add(item["word"].lower())
            added += 1

    for data in [*NEW_TOPICS, *MORE_TOPICS, *PLUS_TOPICS]:
        topic = topics.get(data["slug"])
        if topic is None:
            max_order += 1
            topic = VocabTopic(
                slug=data["slug"],
                title=data["title"],
                description=data["description"],
                level_code=data["level_code"],
                sort_order=max_order,
            )
            db.add(topic)
            db.flush()
            topics[topic.slug] = topic
            existing: set[str] = set()
        else:
            existing = {word.word.lower() for word in topic.words}
        for item in data["words"]:
            if item["word"].lower() in existing:
                continue
            db.add(VocabWord(topic_id=topic.id, **item))
            existing.add(item["word"].lower())
            added += 1
    return added
