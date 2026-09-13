"""Incremental expanders for practice/test banks, modules, study decks, settings."""

from sqlalchemy import inspect, text

from app.core.config import settings
from app.core.security import hash_password
from app.models.grammar import Exam, ExamQuestion, Exercise, GrammarLevel, GrammarModule, Lesson, ModuleTest, TestQuestion
from app.models.settings import SiteSetting
from app.models.study import StudyCard, StudyDeck
from app.models.user import User
from app.models.vocabulary import VocabTopic, VocabWord
from app.seed.extra_banks import practice_bank_for, test_bank_for
from app.seed.extra_exams import EXTRA_EXAMS
from app.seed.extra_vocab import EXTRA_WORDS_BY_SLUG, NEW_TOPICS
from app.seed.more_vocab import MORE_TOPICS, MORE_WORDS_BY_SLUG
from app.seed.plus_vocab import PLUS_TOPICS, PLUS_WORDS_BY_SLUG
from app.seed.study_seed import STUDY_DECKS
from app.seed.topic_banks import (
    BANNED_PROMPTS,
    LEGACY_GENERIC_PRACTICE_PROMPTS,
    LEGACY_GENERIC_TEST_PROMPTS,
)
from app.seed.word_order import WORD_ORDER_MODULES


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


def _add_unique_items(db, *, existing_prompts: set[str], items: list, factory, order_start: int) -> tuple[int, int]:
    added = 0
    order = order_start
    for item in items:
        prompt = item["prompt"] if isinstance(item, dict) else item.prompt
        if prompt in existing_prompts:
            continue
        order += 1
        db.add(factory(order, item))
        existing_prompts.add(prompt)
        added += 1
    return added, order


def _allowed_practice_prompts(slug: str) -> set[str]:
    """Prompts that may remain for this module: seed core + slug banks."""
    from app.seed.a1 import A1
    from app.seed.a2 import A2
    from app.seed.b1 import B1
    from app.seed.b2 import B2
    from app.seed.c1 import C1
    from app.seed.c2 import C2

    allowed: set[str] = set()
    for pack in (A1, A2, B1, B2, C1, C2, WORD_ORDER_MODULES):
        for data in pack:
            if data["slug"] != slug:
                continue
            for item in data.get("exercises", []):
                allowed.add(item["prompt"])
    for item in practice_bank_for(slug):
        allowed.add(item["prompt"])
    return allowed


def _allowed_test_prompts(slug: str) -> set[str]:
    from app.seed.a1 import A1
    from app.seed.a2 import A2
    from app.seed.b1 import B1
    from app.seed.b2 import B2
    from app.seed.c1 import C1
    from app.seed.c2 import C2

    allowed: set[str] = set()
    for pack in (A1, A2, B1, B2, C1, C2, WORD_ORDER_MODULES):
        for data in pack:
            if data["slug"] != slug:
                continue
            for item in data.get("test", []):
                allowed.add(item["prompt"])
    for item in test_bank_for(slug):
        allowed.add(item["prompt"])
    return allowed


def scrub_off_topic_pad_items(db) -> dict[str, int]:
    """Remove banned tips and legacy CEFR-wide pad items from the wrong modules.

    Existing Docker volumes keep rows from GENERIC_*_PAD; this deletes them unless
    the prompt is explicitly allowed for that module's seed/topic bank. Then
    expand_practice_banks / expand_module_tests refill with on-topic items.
    """
    removed_practice = 0
    removed_tests = 0
    modules = db.query(GrammarModule).all()
    for module in modules:
        allow_p = _allowed_practice_prompts(module.slug)
        for ex in list(module.exercises):
            prompt = ex.prompt or ""
            if prompt in BANNED_PROMPTS:
                db.delete(ex)
                removed_practice += 1
                continue
            if prompt in LEGACY_GENERIC_PRACTICE_PROMPTS and prompt not in allow_p:
                db.delete(ex)
                removed_practice += 1
        if not module.test:
            continue
        allow_t = _allowed_test_prompts(module.slug)
        for q in list(module.test.questions):
            prompt = q.prompt or ""
            if prompt in BANNED_PROMPTS:
                db.delete(q)
                removed_tests += 1
                continue
            if prompt in LEGACY_GENERIC_TEST_PROMPTS and prompt not in allow_t:
                db.delete(q)
                removed_tests += 1
    return {"practice": removed_practice, "tests": removed_tests}


def expand_practice_banks(db, minimum: int = 16) -> int:
    """Grow practice banks from slug-keyed EXTRA + TOPIC pads. Never CEFR-wide pads."""
    added = 0
    modules = db.query(GrammarModule).all()
    for module in modules:
        prompts = {ex.prompt for ex in module.exercises}
        order = max((ex.sort_order for ex in module.exercises), default=0)
        lesson_id = module.lessons[0].id if module.lessons else None
        extras = practice_bank_for(module.slug)

        def factory(ord_, item):
            return Exercise(
                module_id=module.id,
                lesson_id=lesson_id,
                sort_order=ord_,
                xp=item.get("xp", 10) if isinstance(item, dict) else 10,
                **_fields(item),
            )

        n, order = _add_unique_items(db, existing_prompts=prompts, items=extras, factory=factory, order_start=order)
        added += n
        # If still short, only cycle the same on-topic bank (no cross-module padding).
        while len(prompts) < minimum:
            before = len(prompts)
            n, order = _add_unique_items(db, existing_prompts=prompts, items=extras, factory=factory, order_start=order)
            added += n
            if len(prompts) == before:
                break
    return added


def expand_module_tests(db, minimum: int = 16) -> int:
    """Grow test banks from slug-keyed EXTRA + TOPIC pads. Do NOT copy practice exercises."""
    added = 0
    tests = db.query(ModuleTest).all()
    for test in tests:
        module = test.module
        practice_prompts = {ex.prompt for ex in module.exercises}
        prompts = {q.prompt for q in test.questions}
        order = max((q.sort_order for q in test.questions), default=0)
        extras = [
            item
            for item in test_bank_for(module.slug)
            if item["prompt"] not in practice_prompts
        ]

        def factory(ord_, item):
            return TestQuestion(test_id=test.id, sort_order=ord_, **_fields(item))

        n, order = _add_unique_items(db, existing_prompts=prompts, items=extras, factory=factory, order_start=order)
        added += n
        while len(prompts) < minimum:
            pad = [item for item in extras if item["prompt"] not in practice_prompts]
            before = len(prompts)
            n, order = _add_unique_items(db, existing_prompts=prompts, items=pad, factory=factory, order_start=order)
            added += n
            if len(prompts) == before:
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


def ensure_word_order_modules(db) -> int:
    """Insert CEFR word-order modules if missing (idempotent by slug)."""
    added = 0
    levels = {level.code: level for level in db.query(GrammarLevel).all()}
    for data in WORD_ORDER_MODULES:
        if db.query(GrammarModule).filter(GrammarModule.slug == data["slug"]).first():
            continue
        level = levels.get(data["level_code"])
        if not level:
            continue
        max_order = (
            db.query(GrammarModule)
            .filter(GrammarModule.level_id == level.id)
            .count()
        )
        gm = GrammarModule(
            level_id=level.id,
            slug=data["slug"],
            title=data["title"],
            description=data["description"],
            sort_order=max_order + 1,
            estimated_minutes=data["minutes"],
            sources=data.get("sources") or [],
        )
        db.add(gm)
        db.flush()
        lesson_data = data["lesson"]
        lesson = Lesson(
            module_id=gm.id,
            title=lesson_data["title"],
            content=lesson_data["content"],
            sort_order=1,
        )
        db.add(lesson)
        db.flush()
        for ex_i, item in enumerate(data["exercises"], start=1):
            db.add(Exercise(module_id=gm.id, lesson_id=lesson.id, sort_order=ex_i, **_fields(item)))
        test = ModuleTest(
            module_id=gm.id,
            title=f"Тест: {data['title']}",
            time_limit_sec=900,
            passing_score=70,
        )
        db.add(test)
        db.flush()
        for q_i, item in enumerate(data["test"], start=1):
            db.add(TestQuestion(test_id=test.id, sort_order=q_i, **_fields(item)))
        added += 1
    return added


def expand_study_decks(db) -> int:
    added = 0
    existing = {deck.slug: deck for deck in db.query(StudyDeck).all()}
    max_order = max((d.sort_order for d in existing.values()), default=0)
    for data in STUDY_DECKS:
        deck = existing.get(data["slug"])
        if deck is None:
            max_order += 1
            deck = StudyDeck(
                slug=data["slug"],
                title=data["title"],
                description=data["description"],
                kind=data["kind"],
                sort_order=max_order,
            )
            db.add(deck)
            db.flush()
            existing[deck.slug] = deck
            known: set[str] = set()
        else:
            known = {card.primary_text.lower() for card in deck.cards}
        order = max((c.sort_order for c in deck.cards), default=0)
        for item in data["cards"]:
            key = item["primary_text"].lower()
            if key in known:
                continue
            order += 1
            db.add(
                StudyCard(
                    deck_id=deck.id,
                    primary_text=item["primary_text"],
                    secondary_text=item.get("secondary_text", ""),
                    tertiary_text=item.get("tertiary_text", ""),
                    translation=item["translation"],
                    example=item.get("example", ""),
                    example_translation=item.get("example_translation", ""),
                    category=item.get("category", ""),
                    sort_order=order,
                )
            )
            known.add(key)
            added += 1
    return added


def fix_known_article_answers(db) -> int:
    """Repair Open ___ door and similar gap/article items in existing DBs."""
    fixed = 0
    repairs = [
        (
            "Open ___ door",
            {
                "kind": "fill_blank",
                "prompt": "Open ___ door. (мы оба видим дверь)",
                "answer": "the",
                "accepted": ["Open the door.", "Open the door", "open the door"],
                "explanation": "Конкретный объект в ситуации — the. Можно ввести the или Open the door.",
            },
        ),
        (
            "I want ___ dog",
            {
                "kind": "fill_blank",
                "prompt": "I want ___ dog. (любая собака)",
                "answer": "a",
                "accepted": ["I want a dog.", "I want a dog"],
                "explanation": "Неопределённый экземпляр класса. Можно a или I want a dog.",
            },
        ),
    ]
    for needle, fields in repairs:
        for model in (Exercise, TestQuestion):
            rows = db.query(model).filter(model.prompt.contains(needle)).all()
            for row in rows:
                for key, value in fields.items():
                    setattr(row, key, value)
                fixed += 1
    return fixed


def rewrite_known_prompts(db) -> int:
    """Update terse transform prompts in live DB (old exact prompt → clearer wording)."""
    from app.seed.prompt_rewrites import EXPLANATION_REWRITES, PROMPT_REWRITES

    fixed = 0
    for old_prompt, new_prompt in PROMPT_REWRITES.items():
        if old_prompt == new_prompt:
            continue
        for model in (Exercise, TestQuestion, ExamQuestion):
            rows = db.query(model).filter(model.prompt == old_prompt).all()
            for row in rows:
                row.prompt = new_prompt
                if old_prompt in EXPLANATION_REWRITES:
                    row.explanation = EXPLANATION_REWRITES[old_prompt]
                fixed += 1
    return fixed


def sync_lesson_theory(db) -> int:
    """Overwrite Lesson.title/content from seed packs by module slug (idempotent).

    Fresh installs already get enriched theory via helpers.module() + THEORY_BY_SLUG.
    Existing DBs pick up richer theory (and scrubs like «развилкать») on the next
    ``python -m app.seed.runner`` without wiping data.
    """
    from app.seed.a1 import A1
    from app.seed.a2 import A2
    from app.seed.b1 import B1
    from app.seed.b2 import B2
    from app.seed.c1 import C1
    from app.seed.c2 import C2

    by_slug: dict[str, dict] = {}
    for pack in (A1, A2, B1, B2, C1, C2, WORD_ORDER_MODULES):
        for data in pack:
            by_slug[data["slug"]] = data["lesson"]

    updated = 0
    modules = db.query(GrammarModule).all()
    for gm in modules:
        seed = by_slug.get(gm.slug)
        if not seed or not gm.lessons:
            continue
        lesson = gm.lessons[0]
        new_title = seed["title"]
        new_content = seed["content"]
        if lesson.title != new_title or lesson.content != new_content:
            lesson.title = new_title
            lesson.content = new_content
            updated += 1
    return updated



def repair_match_options(db) -> int:
    """Ensure match items store {left, right} and aligned a=b answer keys."""
    from app.services.match_format import normalize_match_payload

    fixed = 0
    for model in (Exercise, TestQuestion, ExamQuestion):
        rows = db.query(model).filter(model.kind == "match").all()
        for row in rows:
            sides, aligned = normalize_match_payload(row.options, row.answer)
            if not sides["left"] or not sides["right"]:
                continue
            if row.options != sides or row.answer != aligned:
                row.options = sides
                row.answer = aligned
                fixed += 1
    return fixed


DONATION_MESSAGE = (
    "Если lEarNing помогает учить EN, можно оставить чаевые — это поддерживает развитие курса."
)


def ensure_site_settings(db) -> None:
    row = db.get(SiteSetting, 1)
    if row is None:
        db.add(
            SiteSetting(
                id=1,
                donation_message=DONATION_MESSAGE,
                email_verification_required=settings.EMAIL_VERIFICATION_REQUIRED,
            )
        )
        return
    if "Lumina" in (row.donation_message or ""):
        row.donation_message = DONATION_MESSAGE
    # Column may be missing on older rows until migration helper runs
    if getattr(row, "email_verification_required", None) is None:
        row.email_verification_required = settings.EMAIL_VERIFICATION_REQUIRED


def ensure_email_verified_column(engine) -> None:
    inspector = inspect(engine)
    if "users" not in inspector.get_table_names():
        return
    columns = {column["name"] for column in inspector.get_columns("users")}
    if "email_verified" in columns:
        return
    with engine.begin() as conn:
        conn.execute(text("ALTER TABLE users ADD COLUMN email_verified BOOLEAN NOT NULL DEFAULT TRUE"))


def ensure_site_setting_columns(engine) -> None:
    inspector = inspect(engine)
    if "site_settings" not in inspector.get_table_names():
        return
    columns = {column["name"] for column in inspector.get_columns("site_settings")}
    if "email_verification_required" in columns:
        return
    with engine.begin() as conn:
        conn.execute(
            text(
                "ALTER TABLE site_settings "
                "ADD COLUMN email_verification_required BOOLEAN NOT NULL DEFAULT TRUE"
            )
        )


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
