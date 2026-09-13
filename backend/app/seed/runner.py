"""Seed lEarNinG: CEFR levels, grammar modules, vocabulary, exams, study decks.

Creates an admin only when ADMIN_EMAIL and ADMIN_PASSWORD are both set.
Run: python -m app.seed.runner
"""

from app import models  # noqa: F401 — register metadata
from app.core.database import Base, SessionLocal, engine
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
from app.models.vocabulary import VocabTopic, VocabWord
from app.seed.a1 import A1
from app.seed.a2 import A2
from app.seed.b1 import B1
from app.seed.b2 import B2
from app.seed.c1 import C1
from app.seed.c2 import C2
from app.seed.exams import EXAMS
from app.seed.levels import LEVELS
from app.seed.expand import (
    ensure_admin_from_env,
    ensure_assessment_attempt_columns,
    ensure_email_verified_column,
    ensure_site_setting_columns,
    ensure_site_settings,
    ensure_vocab_mastery_column,
    ensure_word_order_modules,
    expand_exams,
    expand_module_tests,
    expand_practice_banks,
    expand_study_decks,
    expand_skills,
    expand_vocabulary,
    fix_known_article_answers,
    fix_match_answer_leaks,
    remove_legacy_demo_accounts,
    repair_match_options,
    rewrite_known_prompts,
    scrub_duplicate_prompts,
    scrub_off_topic_pad_items,
    sync_lesson_theory,
)
from app.seed.vocab import TOPICS


def _item_fields(item: dict) -> dict:
    return {
        "kind": item["kind"],
        "prompt": item["prompt"],
        "options": item.get("options"),
        "answer": item["answer"],
        "accepted": item.get("accepted"),
        "explanation": item["explanation"],
    }


def seed_modules(db, levels_by_code: dict[str, GrammarLevel]) -> tuple[int, int, int, int]:
    packs = [
        ("A1", A1),
        ("A2", A2),
        ("B1", B1),
        ("B2", B2),
        ("C1", C1),
        ("C2", C2),
    ]
    n_modules = n_lessons = n_exercises = n_questions = 0
    for code, modules in packs:
        level = levels_by_code[code]
        for index, data in enumerate(modules, start=1):
            gm = GrammarModule(
                level_id=level.id,
                slug=data["slug"],
                title=data["title"],
                description=data["description"],
                sort_order=index,
                estimated_minutes=data["minutes"],
                sources=data.get("sources") or [],
            )
            db.add(gm)
            db.flush()
            n_modules += 1

            lesson_data = data["lesson"]
            lesson = Lesson(
                module_id=gm.id,
                title=lesson_data["title"],
                content=lesson_data["content"],
                sort_order=1,
            )
            db.add(lesson)
            db.flush()
            n_lessons += 1

            for ex_i, item in enumerate(data["exercises"], start=1):
                db.add(
                    Exercise(
                        module_id=gm.id,
                        lesson_id=lesson.id,
                        sort_order=ex_i,
                        **_item_fields(item),
                    )
                )
                n_exercises += 1

            test = ModuleTest(
                module_id=gm.id,
                title=f"Тест: {data['title']}",
                time_limit_sec=600,
                passing_score=70,
            )
            db.add(test)
            db.flush()

            for q_i, item in enumerate(data["test"], start=1):
                db.add(
                    TestQuestion(
                        test_id=test.id,
                        sort_order=q_i,
                        **_item_fields(item),
                    )
                )
                n_questions += 1
    return n_modules, n_lessons, n_exercises, n_questions


def _run_expanders(db) -> dict:
    scrubbed = scrub_off_topic_pad_items(db)
    stats = {
        "scrub_practice": scrubbed["practice"],
        "scrub_tests": scrubbed["tests"],
        "word_order": ensure_word_order_modules(db),
        "theory": sync_lesson_theory(db),
        "practice": expand_practice_banks(db),
        "tests": expand_module_tests(db),
        "exams": expand_exams(db),
        "words": expand_vocabulary(db),
        "study": expand_study_decks(db),
        "skills": expand_skills(db),
        "article_fixes": fix_known_article_answers(db),
        "match_leak_fixes": fix_match_answer_leaks(db),
        "prompt_rewrites": rewrite_known_prompts(db),
        "match_repairs": repair_match_options(db),
    }
    # After rewrites, collapse same-prompt collisions left in existing DBs.
    dupes = scrub_duplicate_prompts(db)
    stats["scrub_dup_practice"] = dupes["practice"]
    stats["scrub_dup_tests"] = dupes["tests"]
    stats["scrub_dup_exams"] = dupes["exams"]
    return stats


def main() -> None:
    Base.metadata.create_all(bind=engine)
    ensure_email_verified_column(engine)
    ensure_site_setting_columns(engine)
    ensure_vocab_mastery_column(engine)
    ensure_assessment_attempt_columns(engine)
    db = SessionLocal()
    try:
        already = db.query(GrammarLevel).first() is not None
        if already:
            stats = _run_expanders(db)
            ensure_site_settings(db)
            removed_demo = remove_legacy_demo_accounts(db)
            created_admin = ensure_admin_from_env(db)
            db.commit()
            print(
                "already seeded; "
                f"scrub_practice=-{stats['scrub_practice']}, scrub_tests=-{stats['scrub_tests']}, "
                f"scrub_dup_practice=-{stats['scrub_dup_practice']}, "
                f"scrub_dup_tests=-{stats['scrub_dup_tests']}, "
                f"scrub_dup_exams=-{stats['scrub_dup_exams']}, "
                f"word_order +{stats['word_order']}, theory={stats['theory']}, "
                f"practice +{stats['practice']}, "
                f"tests +{stats['tests']}, exams +{stats['exams']}, words +{stats['words']}, "
                f"study +{stats['study']}, skills +{stats['skills']}, article_fixes={stats['article_fixes']}, "
                f"match_leak_fixes={stats['match_leak_fixes']}, "
                f"prompt_rewrites={stats['prompt_rewrites']}, "
                f"match_repairs={stats['match_repairs']}; "
                f"demo_removed={removed_demo}; admin={'created' if created_admin else 'unchanged'}"
            )
            return

        created_admin = ensure_admin_from_env(db)
        removed_demo = remove_legacy_demo_accounts(db)

        levels_by_code: dict[str, GrammarLevel] = {}
        for row in LEVELS:
            level = GrammarLevel(**row)
            db.add(level)
            db.flush()
            levels_by_code[level.code] = level

        n_modules, n_lessons, n_exercises, n_test_q = seed_modules(db, levels_by_code)

        n_topics = n_words = 0
        for index, topic in enumerate(TOPICS, start=1):
            vt = VocabTopic(
                slug=topic["slug"],
                title=topic["title"],
                description=topic["description"],
                level_code=topic["level_code"],
                sort_order=index,
            )
            db.add(vt)
            db.flush()
            n_topics += 1
            for word in topic["words"]:
                db.add(VocabWord(topic_id=vt.id, **word))
                n_words += 1

        n_exams = n_exam_q = 0
        for exam in EXAMS:
            row = Exam(
                level_id=levels_by_code[exam["level_code"]].id,
                title=exam["title"],
                description=exam["description"],
                time_limit_sec=exam["time_limit_sec"],
                passing_score=exam["passing_score"],
            )
            db.add(row)
            db.flush()
            n_exams += 1
            for q_i, item in enumerate(exam["questions"], start=1):
                db.add(
                    ExamQuestion(
                        exam_id=row.id,
                        sort_order=q_i,
                        **_item_fields(item),
                    )
                )
                n_exam_q += 1

        stats = _run_expanders(db)
        ensure_site_settings(db)
        removed_demo += remove_legacy_demo_accounts(db)
        db.commit()
        print(
            "seeded: "
            f"admin={'created' if created_admin else 'skipped'} demo_removed={removed_demo} "
            f"levels={len(LEVELS)} modules={n_modules + stats['word_order']} lessons={n_lessons} "
            f"exercises={n_exercises + stats['practice']} test_questions={n_test_q + stats['tests']} "
            f"topics={n_topics} words={n_words + stats['words']} exams={n_exams} "
            f"exam_questions={n_exam_q + stats['exams']} study_cards=+{stats['study']} "
            f"skills=+{stats['skills']} "
            f"scrub_practice=-{stats['scrub_practice']} scrub_tests=-{stats['scrub_tests']} "
            f"scrub_dup_practice=-{stats['scrub_dup_practice']} "
            f"scrub_dup_tests=-{stats['scrub_dup_tests']} "
            f"scrub_dup_exams=-{stats['scrub_dup_exams']} "
            f"theory={stats['theory']} "
            f"prompt_rewrites={stats['prompt_rewrites']} match_repairs={stats['match_repairs']}"
        )
    finally:
        db.close()


if __name__ == "__main__":
    main()
