"""Global product search across grammar, vocab, study, skills, exams, phonetics, and static routes."""

from __future__ import annotations

from fastapi import APIRouter, Depends, Query
from sqlalchemy import or_
from sqlalchemy.orm import Session, joinedload

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.grammar import Exam, GrammarLevel, GrammarModule, Lesson
from app.models.skills import SkillItem
from app.models.study import StudyCard, StudyDeck
from app.models.user import User
from app.models.vocabulary import VocabTopic, VocabWord
from app.seed.phonetics import TOPICS

router = APIRouter(prefix="/search", tags=["search"])

RESULT_CAP = 25
PER_SOURCE_CAP = 8
HIGHLIGHT_BATCH = 10

STUDY_SECTIONS = {
    "verbs": "Глаголы",
    "idioms": "Идиомы",
    "exceptions": "Исключения",
}
STUDY_PATHS = {
    "verbs": "verbs",
    "idioms": "idioms",
    "exceptions": "exceptions",
}
SKILL_SECTIONS = {
    "reading": "Чтение",
    "listening": "Слушание",
    "dialogue": "Диалоги",
}
SKILL_PATHS = {
    "reading": "reading",
    "listening": "listening",
    "dialogue": "dialogues",
}

STATIC_ROUTES = [
    {"section": "Обзор", "title": "Обзор", "subtitle": "Главная страница кабинета", "href": "/app"},
    {"section": "Грамматика", "title": "Грамматика", "subtitle": "Уровни и модули", "href": "/app/grammar"},
    {"section": "Звуки", "title": "Звуки", "subtitle": "Фонетика и произношение", "href": "/app/sounds"},
    {"section": "Словарь", "title": "Словарь", "subtitle": "Темы и слова", "href": "/app/vocab"},
    {"section": "Глаголы", "title": "Неправильные глаголы", "subtitle": "Колоды для заучивания", "href": "/app/verbs"},
    {"section": "Идиомы", "title": "Идиомы и пословицы", "subtitle": "Колоды для заучивания", "href": "/app/idioms"},
    {"section": "Исключения", "title": "Исключения", "subtitle": "Орфография и особые случаи", "href": "/app/exceptions"},
    {"section": "Чтение", "title": "Чтение", "subtitle": "Тексты с заданиями", "href": "/app/reading"},
    {"section": "Слушание", "title": "Слушание", "subtitle": "Аудио и диктанты", "href": "/app/listening"},
    {"section": "Диалоги", "title": "Диалоги", "subtitle": "Мини-сцены", "href": "/app/dialogues"},
    {"section": "Экзамены", "title": "Экзамены", "subtitle": "Проверка по уровням", "href": "/app/exams"},
    {"section": "Справка", "title": "Справка", "subtitle": "Типы упражнений и подсказки", "href": "/app/help"},
    {"section": "Профиль", "title": "Профиль", "subtitle": "Имя, пароль и прогресс", "href": "/app/profile"},
]


def _ilike(pattern: str):
    return f"%{pattern}%"


def _rank(query: str, *fields: str | None) -> int:
    """Lower score is better. Prefer title/prefix hits over fuzzy description matches."""
    q = query.casefold().strip()
    if not q:
        return 999
    best = 900
    for index, raw in enumerate(fields):
        if not raw:
            continue
        text = str(raw).casefold()
        weight = index * 40
        if text == q:
            best = min(best, weight)
        elif text.startswith(q):
            best = min(best, 10 + weight)
        elif q in text:
            best = min(best, 30 + weight)
    return best


def _hit(section: str, title: str, href: str, subtitle: str | None = None, rank: int = 100) -> dict:
    item = {"section": section, "title": title, "href": href, "_rank": rank}
    if subtitle:
        item["subtitle"] = subtitle
    return item


def _dedupe(hits: list[dict]) -> list[dict]:
    seen: set[str] = set()
    out: list[dict] = []
    for hit in hits:
        key = hit["href"]
        # Allow same href with different subtitles (e.g. several words → one topic)
        if hit.get("subtitle"):
            key = f"{hit['href']}|{hit['subtitle']}"
        if key in seen:
            continue
        seen.add(key)
        out.append(hit)
    return out


def _search_static(q: str) -> list[dict]:
    hits = []
    for route in STATIC_ROUTES:
        rank = _rank(q, route["title"], route["section"], route.get("subtitle"))
        if rank < 900:
            hits.append(
                _hit(
                    route["section"],
                    route["title"],
                    route["href"],
                    route.get("subtitle"),
                    rank=rank + 5,
                )
            )
    return hits[:PER_SOURCE_CAP]


def _search_grammar(db: Session, q: str, pattern: str) -> list[dict]:
    hits: list[dict] = []

    levels = (
        db.query(GrammarLevel)
        .filter(
            or_(
                GrammarLevel.title.ilike(pattern),
                GrammarLevel.subtitle.ilike(pattern),
                GrammarLevel.description.ilike(pattern),
                GrammarLevel.code.ilike(pattern),
            )
        )
        .order_by(GrammarLevel.sort_order)
        .limit(PER_SOURCE_CAP)
        .all()
    )
    for level in levels:
        hits.append(
            _hit(
                "Грамматика",
                level.title,
                f"/app/grammar?highlight={level.code}",
                level.subtitle or level.code,
                rank=_rank(q, level.title, level.code, level.subtitle, level.description),
            )
        )

    modules = (
        db.query(GrammarModule)
        .options(joinedload(GrammarModule.level))
        .filter(
            or_(
                GrammarModule.title.ilike(pattern),
                GrammarModule.description.ilike(pattern),
                GrammarModule.slug.ilike(pattern),
            )
        )
        .order_by(GrammarModule.sort_order)
        .limit(PER_SOURCE_CAP)
        .all()
    )
    for module in modules:
        level_title = module.level.title if module.level else None
        level_code = module.level.code if module.level else None
        href = (
            f"/app/grammar/{level_code}?highlight={module.slug}"
            if level_code
            else f"/app/module/{module.slug}"
        )
        hits.append(
            _hit(
                "Грамматика",
                module.title,
                href,
                level_title,
                rank=_rank(q, module.title, module.description) + 2,
            )
        )

    lessons = (
        db.query(Lesson)
        .options(joinedload(Lesson.module).joinedload(GrammarModule.level))
        .filter(Lesson.title.ilike(pattern))
        .order_by(Lesson.sort_order)
        .limit(PER_SOURCE_CAP)
        .all()
    )
    for lesson in lessons:
        module = lesson.module
        if not module:
            continue
        crumbs = module.title
        if module.level:
            crumbs = f"{module.level.title} → {module.title}"
        hits.append(
            _hit(
                "Грамматика",
                lesson.title,
                f"/app/module/{module.slug}/lesson/{lesson.id}",
                crumbs,
                rank=_rank(q, lesson.title) + 4,
            )
        )

    return hits


def _search_phonetics(q: str) -> list[dict]:
    hits = []
    for topic in TOPICS:
        rank = _rank(q, topic["title"], topic["description"], topic["slug"])
        if rank < 900:
            hits.append(
                _hit(
                    "Звуки",
                    topic["title"],
                    f"/app/sounds?highlight={topic['slug']}",
                    topic.get("description"),
                    rank=rank,
                )
            )
    hits.sort(key=lambda item: item["_rank"])
    return hits[:PER_SOURCE_CAP]


def _search_vocab(db: Session, q: str, pattern: str) -> list[dict]:
    hits: list[dict] = []

    topics = (
        db.query(VocabTopic)
        .filter(
            or_(
                VocabTopic.title.ilike(pattern),
                VocabTopic.description.ilike(pattern),
                VocabTopic.slug.ilike(pattern),
            )
        )
        .order_by(VocabTopic.sort_order)
        .limit(PER_SOURCE_CAP)
        .all()
    )
    for topic in topics:
        hits.append(
            _hit(
                "Словарь",
                topic.title,
                f"/app/vocab?highlight={topic.slug}",
                topic.description or topic.level_code,
                rank=_rank(q, topic.title, topic.description),
            )
        )

    words = (
        db.query(VocabWord)
        .options(joinedload(VocabWord.topic))
        .filter(
            or_(
                VocabWord.word.ilike(pattern),
                VocabWord.translation.ilike(pattern),
            )
        )
        .limit(PER_SOURCE_CAP)
        .all()
    )
    for word in words:
        topic = word.topic
        if not topic:
            continue
        matched = word.word if q.casefold() in word.word.casefold() else word.translation
        siblings = (
            db.query(VocabWord.id)
            .filter(VocabWord.topic_id == topic.id)
            .order_by(VocabWord.id)
            .all()
        )
        ids = [row[0] for row in siblings]
        try:
            batch = ids.index(word.id) // HIGHLIGHT_BATCH + 1
        except ValueError:
            batch = 1
        hits.append(
            _hit(
                "Словарь",
                topic.title,
                f"/app/vocab/{topic.slug}?batch={batch}&highlight={word.id}",
                matched,
                rank=_rank(q, word.word, word.translation) + 8,
            )
        )

    return hits


def _search_study(db: Session, q: str, pattern: str) -> list[dict]:
    hits: list[dict] = []

    decks = (
        db.query(StudyDeck)
        .filter(
            or_(
                StudyDeck.title.ilike(pattern),
                StudyDeck.description.ilike(pattern),
                StudyDeck.slug.ilike(pattern),
            )
        )
        .order_by(StudyDeck.sort_order)
        .limit(PER_SOURCE_CAP)
        .all()
    )
    for deck in decks:
        section = STUDY_SECTIONS.get(deck.kind, "Учёба")
        path = STUDY_PATHS.get(deck.kind, deck.kind)
        hits.append(
            _hit(
                section,
                deck.title,
                f"/app/{path}?highlight={deck.slug}",
                deck.description or None,
                rank=_rank(q, deck.title, deck.description),
            )
        )

    cards = (
        db.query(StudyCard)
        .options(joinedload(StudyCard.deck))
        .filter(
            or_(
                StudyCard.primary_text.ilike(pattern),
                StudyCard.secondary_text.ilike(pattern),
                StudyCard.tertiary_text.ilike(pattern),
                StudyCard.translation.ilike(pattern),
            )
        )
        .limit(PER_SOURCE_CAP)
        .all()
    )
    for card in cards:
        deck = card.deck
        if not deck:
            continue
        section = STUDY_SECTIONS.get(deck.kind, "Учёба")
        path = STUDY_PATHS.get(deck.kind, deck.kind)
        term = card.primary_text
        for candidate in (card.primary_text, card.secondary_text, card.tertiary_text, card.translation):
            if candidate and q.casefold() in candidate.casefold():
                term = candidate
                break
        siblings = (
            db.query(StudyCard.id)
            .filter(StudyCard.deck_id == deck.id)
            .order_by(StudyCard.sort_order, StudyCard.id)
            .all()
        )
        ids = [row[0] for row in siblings]
        try:
            batch = ids.index(card.id) // HIGHLIGHT_BATCH + 1
        except ValueError:
            batch = 1
        hits.append(
            _hit(
                section,
                deck.title,
                f"/app/{path}/{deck.slug}?batch={batch}&highlight={card.id}",
                term,
                rank=_rank(q, card.primary_text, card.translation, card.secondary_text) + 8,
            )
        )

    return hits


def _search_skills(db: Session, q: str, pattern: str) -> list[dict]:
    hits: list[dict] = []
    items = (
        db.query(SkillItem)
        .filter(
            or_(
                SkillItem.title.ilike(pattern),
                SkillItem.description.ilike(pattern),
                SkillItem.slug.ilike(pattern),
            )
        )
        .order_by(SkillItem.sort_order)
        .limit(PER_SOURCE_CAP)
        .all()
    )
    for item in items:
        section = SKILL_SECTIONS.get(item.kind, "Навыки")
        path = SKILL_PATHS.get(item.kind, item.kind)
        hits.append(
            _hit(
                section,
                item.title,
                f"/app/{path}?highlight={item.slug}",
                item.description or item.level_code,
                rank=_rank(q, item.title, item.description),
            )
        )
    return hits


def _search_exams(db: Session, q: str, pattern: str) -> list[dict]:
    hits: list[dict] = []
    exams = (
        db.query(Exam)
        .options(joinedload(Exam.level))
        .filter(
            or_(
                Exam.title.ilike(pattern),
                Exam.description.ilike(pattern),
            )
        )
        .limit(PER_SOURCE_CAP)
        .all()
    )
    for exam in exams:
        level_title = exam.level.title if exam.level else None
        hits.append(
            _hit(
                "Экзамены",
                exam.title,
                f"/app/exams?highlight={exam.id}",
                level_title or exam.description or None,
                rank=_rank(q, exam.title, exam.description),
            )
        )
    return hits


@router.get("")
def global_search(
    q: str = Query("", min_length=0, max_length=120),
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    query = (q or "").strip()
    if len(query) < 2:
        return {"query": query, "results": []}

    pattern = _ilike(query)
    hits: list[dict] = []
    hits.extend(_search_static(query))
    hits.extend(_search_grammar(db, query, pattern))
    hits.extend(_search_phonetics(query))
    hits.extend(_search_vocab(db, query, pattern))
    hits.extend(_search_study(db, query, pattern))
    hits.extend(_search_skills(db, query, pattern))
    hits.extend(_search_exams(db, query, pattern))

    hits = _dedupe(hits)
    hits.sort(key=lambda item: (item["_rank"], item["section"], item["title"]))
    results = []
    for hit in hits[:RESULT_CAP]:
        item = {"section": hit["section"], "title": hit["title"], "href": hit["href"]}
        if hit.get("subtitle"):
            item["subtitle"] = hit["subtitle"]
        results.append(item)

    return {"query": query, "results": results}
