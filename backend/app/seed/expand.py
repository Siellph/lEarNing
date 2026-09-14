"""Incremental expanders for practice/test banks, modules, study decks, settings."""

from sqlalchemy import inspect, text

from app.core.config import settings
from app.core.security import hash_password
from app.models.grammar import Exam, ExamQuestion, Exercise, GrammarLevel, GrammarModule, Lesson, ModuleTest, TestQuestion
from app.models.settings import SiteSetting
from app.models.study import StudyCard, StudyDeck
from app.models.skills import SkillItem, SkillQuestion
from app.models.user import User
from app.models.vocabulary import VocabTopic, VocabWord
from app.seed.extra_banks import practice_bank_for, test_bank_for
from app.seed.extra_exams import EXTRA_EXAMS
from app.seed.extra_vocab import EXTRA_WORDS_BY_SLUG, NEW_TOPICS
from app.seed.more_vocab import MORE_TOPICS, MORE_WORDS_BY_SLUG
from app.seed.plus_vocab import PLUS_TOPICS, PLUS_WORDS_BY_SLUG
from app.seed.skills_seed import SKILL_ITEMS
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
    """Create missing study decks with all seed cards; never refill an existing deck.

    Once a deck slug exists (even with zero cards after admin deletes), startup seed
    must not re-insert cards — otherwise hard-deletes undo on container restart.
    """
    added = 0
    skipped_decks = 0
    existing = {deck.slug: deck for deck in db.query(StudyDeck).all()}
    max_order = max((d.sort_order for d in existing.values()), default=0)
    for data in STUDY_DECKS:
        if data["slug"] in existing:
            skipped_decks += 1
            continue
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
        for order, item in enumerate(data["cards"], start=1):
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
            added += 1
    if skipped_decks:
        print(f"  study: skipped card insert for {skipped_decks} existing decks")
    return added


def expand_skills(db) -> int:
    """Create missing skill items; for existing items append seed questions missing by prompt.

    Never overwrites existing question rows (preserves admin edits). New prompts from seed
    are inserted with sort_order after the current max for that item.
    """
    added = 0
    existing = {item.slug: item for item in db.query(SkillItem).all()}
    max_order = max((i.sort_order for i in existing.values()), default=0)
    appended_items = 0

    def _insert_question(item: SkillItem, qdata: dict, sort_order: int) -> None:
        nonlocal added
        db.add(
            SkillQuestion(
                item_id=item.id,
                kind=qdata["kind"],
                prompt=qdata["prompt"],
                options=qdata.get("options"),
                answer=qdata["answer"],
                accepted=qdata.get("accepted"),
                speak=qdata.get("speak", ""),
                explanation=qdata.get("explanation", ""),
                sort_order=sort_order,
            )
        )
        added += 1

    for data in SKILL_ITEMS:
        slug = data["slug"]
        seed_questions = data.get("questions") or []
        if slug in existing:
            item = existing[slug]
            # Append-only: insert seed questions whose prompt is not already present.
            have = {
                row.prompt
                for row in db.query(SkillQuestion.prompt).filter(SkillQuestion.item_id == item.id)
            }
            max_q = (
                db.query(SkillQuestion.sort_order)
                .filter(SkillQuestion.item_id == item.id)
                .order_by(SkillQuestion.sort_order.desc())
                .limit(1)
                .scalar()
            )
            next_order = int(max_q or 0)
            item_added = 0
            for qdata in seed_questions:
                prompt = qdata.get("prompt") or ""
                if not prompt or prompt in have:
                    continue
                next_order += 1
                _insert_question(item, qdata, next_order)
                have.add(prompt)
                item_added += 1
            if item_added:
                appended_items += 1
            continue

        max_order += 1
        item = SkillItem(
            slug=slug,
            title=data["title"],
            description=data.get("description", ""),
            kind=data["kind"],
            level_code=data.get("level_code", "A1"),
            body=data.get("body", ""),
            lines=data.get("lines") or [],
            keywords=data.get("keywords") or [],
            sort_order=max_order,
        )
        db.add(item)
        db.flush()
        existing[item.slug] = item
        for qi, qdata in enumerate(seed_questions, start=1):
            _insert_question(item, qdata, qi)

    if appended_items:
        print(f"  skills: appended new questions to {appended_items} existing items")
    return added


def fix_known_article_answers(db) -> int:
    """Disabled: do not overwrite existing exercise/test prompt/answer text on seed."""
    return 0


def fix_match_answer_leaks(db) -> int:
    """Disabled: do not overwrite existing match prompt/options/answer on seed."""
    return 0


def rewrite_known_prompts(db) -> int:
    """Disabled: do not rewrite prompt/answer/explanation on existing rows (preserves admin edits)."""
    return 0


def scrub_duplicate_prompts(db) -> dict[str, int]:
    """Delete extra rows that share the same prompt within one practice/test/exam bank.

    Keeps the lowest-id row. Idempotent; does not wipe banks.
    """
    removed = {"practice": 0, "tests": 0, "exams": 0}

    def _scrub(model, fk: str, bucket: str) -> None:
        rows = db.query(model).order_by(model.id.asc()).all()
        seen: dict[tuple, int] = {}
        for row in rows:
            key = (getattr(row, fk), row.prompt or "")
            if key[1] == "":
                continue
            if key in seen:
                db.delete(row)
                removed[bucket] += 1
            else:
                seen[key] = row.id

    _scrub(Exercise, "module_id", "practice")
    _scrub(TestQuestion, "test_id", "tests")
    _scrub(ExamQuestion, "exam_id", "exams")
    return removed


def sync_lesson_theory(db) -> int:
    """Disabled by default: do not overwrite Lesson.title/content (preserves admin edits).

    Fresh installs still get theory via helpers.module() / initial seed_modules.
    """
    return 0


# Slugs whose theory overlays were fact-checked and corrected; expand may push these only.
THEORY_FIX_SLUGS: list[str] = []


def sync_lesson_theory_for_slugs(db, exclude_slugs: list[str] | None = None) -> int:
    """Overwrite Lesson.content from THEORY_BY_SLUG for all modules 
    EXCEPT those listed in exclude_slugs (or THEORY_FIX_SLUGS).
    """
    from app.models.grammar import GrammarModule
    from app.seed.theory_content import THEORY_BY_SLUG

    excluded = set(exclude_slugs if exclude_slugs is not None else THEORY_FIX_SLUGS)

    modules = db.query(GrammarModule).all()
    updated = 0
    for module in modules:
        if module.slug in excluded:
            continue
        overlay = THEORY_BY_SLUG.get(module.slug)
        if not overlay or not module.lessons:
            continue
        # Prefer primary lesson (sort_order 1); fall back to first.
        lesson = sorted(module.lessons, key=lambda L: L.sort_order)[0]
        lesson.content = overlay
        updated += 1
    return updated


def _collect_seed_match_items() -> list[dict]:
    """All authored match exercises (core modules + topic/extra banks + exams)."""
    from app.seed.a1 import A1
    from app.seed.a2 import A2
    from app.seed.b1 import B1
    from app.seed.b2 import B2
    from app.seed.c1 import C1
    from app.seed.c2 import C2
    from app.seed.exams import EXAMS
    from app.seed.extra_banks import EXTRA_PRACTICE, EXTRA_TEST
    from app.seed.extra_exams import EXTRA_EXAMS
    from app.seed.topic_banks import TOPIC_PRACTICE, TOPIC_TEST

    items: list[dict] = []

    def add(item):
        if isinstance(item, dict) and item.get("kind") == "match":
            items.append(item)

    for pack in (A1, A2, B1, B2, C1, C2, WORD_ORDER_MODULES):
        for data in pack:
            for item in data.get("exercises", []):
                add(item)
            for item in data.get("test", []):
                add(item)

    for bank in (TOPIC_PRACTICE, TOPIC_TEST, EXTRA_PRACTICE, EXTRA_TEST):
        for rows in bank.values():
            for item in rows:
                add(item)

    for exam in EXAMS:
        for item in exam.get("questions", []):
            add(item)
    for rows in EXTRA_EXAMS.values():
        for item in rows:
            add(item)

    return items


def _pick_seed_match(row, seeds: list[dict]) -> dict | None:
    """Choose the best seed match for a DB row (same prompt; prefer left overlap)."""
    candidates = [s for s in seeds if s.get("prompt") == row.prompt]
    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]

    row_left: set[str] = set()
    opts = row.options
    if isinstance(opts, dict):
        row_left = {str(x) for x in (opts.get("left") or [])}
    elif isinstance(opts, list):
        row_left = {str(x) for x in opts}
    answer = (row.answer or "").lower()

    def score(seed: dict) -> tuple[int, int]:
        seed_left = set((seed.get("options") or {}).get("left") or [])
        overlap = len(row_left & seed_left)
        # Disambiguate duplicate prompts like «Паттерны» / «Соедините маркер и время»
        blob = " ".join(seed_left) + " " + (seed.get("answer") or "")
        hint = 0
        if row_left & seed_left:
            hint += 2
        if any(tok in answer for tok in seed_left if len(tok) > 2):
            hint += 1
        if "avoid" in blob.lower() and ("avoid" in answer or any("avoid" in x.lower() for x in row_left)):
            hint += 3
        if "enjoy" in blob.lower() and ("enjoy" in answer or any("enjoy" in x.lower() for x in row_left)):
            hint += 3
        if "yesterday" in blob.lower() and ("yesterday" in answer or "yesterday" in " ".join(row_left).lower()):
            hint += 3
        if "ago" in blob.lower() and ("ago" in answer or "ago" in " ".join(row_left).lower()):
            hint += 3
        return (overlap + hint, len(seed_left))

    return max(candidates, key=score)


def repair_match_options(db) -> int:
    """Disabled: do not re-apply seed match options/answers onto existing rows."""
    return 0


DONATION_MESSAGE = (
    "Если lEarNinG помогает учить ENG, можно оставить чаевые — это поддерживает развитие курса."
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
    if "Lumina" in (row.donation_message or "") or "lEarNing" in (row.donation_message or ""):
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


def ensure_vocab_mastery_column(engine) -> None:
    """Add mastery bitmask; treat former strength>=3 rows as fully learned."""
    inspector = inspect(engine)
    if "vocab_progress" not in inspector.get_table_names():
        return
    columns = {column["name"] for column in inspector.get_columns("vocab_progress")}
    if "mastery" in columns:
        return
    with engine.begin() as conn:
        conn.execute(text("ALTER TABLE vocab_progress ADD COLUMN mastery INTEGER NOT NULL DEFAULT 0"))
        conn.execute(text("UPDATE vocab_progress SET mastery = 15 WHERE strength >= 3"))


def ensure_study_mastery_column(engine) -> None:
    """Add study mastery bitmask; treat former strength>=3 rows as both directions done."""
    inspector = inspect(engine)
    if "study_progress" not in inspector.get_table_names():
        return
    columns = {column["name"] for column in inspector.get_columns("study_progress")}
    if "mastery" in columns:
        return
    with engine.begin() as conn:
        conn.execute(text("ALTER TABLE study_progress ADD COLUMN mastery INTEGER NOT NULL DEFAULT 0"))
        conn.execute(text("UPDATE study_progress SET mastery = 3 WHERE strength >= 3"))


def ensure_assessment_attempt_columns(engine) -> None:
    """Add in-progress attempt fields for module tests and exams without wiping data."""
    inspector = inspect(engine)
    for table in ("test_attempts", "exam_attempts"):
        if table not in inspector.get_table_names():
            continue
        columns = {column["name"]: column for column in inspector.get_columns(table)}
        with engine.begin() as conn:
            if "status" not in columns:
                conn.execute(
                    text(
                        f"ALTER TABLE {table} ADD COLUMN status VARCHAR(20) NOT NULL DEFAULT 'submitted'"
                    )
                )
            if "question_ids" not in columns:
                conn.execute(
                    text(
                        f"ALTER TABLE {table} ADD COLUMN question_ids JSONB NOT NULL DEFAULT '[]'::jsonb"
                    )
                )
            if "details" not in columns:
                conn.execute(text(f"ALTER TABLE {table} ADD COLUMN details JSONB"))
            if "started_at" not in columns:
                conn.execute(text(f"ALTER TABLE {table} ADD COLUMN started_at TIMESTAMPTZ"))
                conn.execute(text(f"UPDATE {table} SET started_at = created_at WHERE started_at IS NULL"))
            if "ends_at" not in columns:
                conn.execute(text(f"ALTER TABLE {table} ADD COLUMN ends_at TIMESTAMPTZ"))
            score_col = columns.get("score")
            if score_col is not None and not score_col.get("nullable", True):
                conn.execute(text(f"ALTER TABLE {table} ALTER COLUMN score DROP NOT NULL"))
            passed_col = columns.get("passed")
            if passed_col is not None and not passed_col.get("nullable", True):
                conn.execute(text(f"ALTER TABLE {table} ALTER COLUMN passed DROP NOT NULL"))
            answers_col = columns.get("answers")
            if answers_col is not None and not answers_col.get("nullable", True):
                # Keep NOT NULL but ensure default for new rows via app; backfill nulls if any
                conn.execute(text(f"UPDATE {table} SET answers = '{{}}'::jsonb WHERE answers IS NULL"))


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


def expand_vocabulary(db, *, refill_existing: bool = False) -> int:
    """Create missing vocab topics with words.

    refill_existing=False (restarts): never add words to an existing topic so
    admin deletes stick; brand-new topic slugs are still created once.
    refill_existing=True (fresh install): also insert missing EXTRA pack words
    into topics that already received core TOPICS seed.
    """
    added = 0
    skipped_topics = 0
    topics = {topic.slug: topic for topic in db.query(VocabTopic).all()}
    max_order = max((topic.sort_order for topic in topics.values()), default=0)

    extra_by_slug: dict[str, list] = {}
    for mapping in (EXTRA_WORDS_BY_SLUG, MORE_WORDS_BY_SLUG, PLUS_WORDS_BY_SLUG):
        for slug, words in mapping.items():
            extra_by_slug.setdefault(slug, []).extend(words)

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
            pack_words = list(data["words"]) + list(extra_by_slug.get(data["slug"], []))
        elif not refill_existing:
            skipped_topics += 1
            continue
        else:
            existing = {word.word.lower() for word in topic.words}
            pack_words = list(data["words"])
        for item in pack_words:
            if item["word"].lower() in existing:
                continue
            db.add(VocabWord(topic_id=topic.id, **item))
            existing.add(item["word"].lower())
            added += 1

    for slug, words in extra_by_slug.items():
        topic = topics.get(slug)
        if topic is None:
            continue
        if not refill_existing:
            skipped_topics += 1
            continue
        existing = {word.word.lower() for word in topic.words}
        for item in words:
            if item["word"].lower() in existing:
                continue
            db.add(VocabWord(topic_id=topic.id, **item))
            existing.add(item["word"].lower())
            added += 1

    if skipped_topics:
        print(f"  vocab: skipped word insert for {skipped_topics} existing topics")
    return added
