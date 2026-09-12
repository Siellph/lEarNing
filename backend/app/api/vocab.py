import math
import random
import re
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.user import User
from app.models.vocabulary import VocabProgress, VocabTopic, VocabWord
from app.schemas.content import VocabCheckIn
from app.services.scoring import is_correct, touch_user

router = APIRouter(prefix="/vocab", tags=["vocab"])

BATCH_SIZE = 10
REVIEW_LIMIT = 3
LEARNED_STRENGTH = 3


def _topic_words(db: Session, topic: VocabTopic) -> list[VocabWord]:
    return db.query(VocabWord).filter(VocabWord.topic_id == topic.id).order_by(VocabWord.id).all()


def _progress_maps(db: Session, user_id: int, word_ids: list[int]) -> tuple[dict[int, int], dict[int, datetime | None]]:
    if not word_ids:
        return {}, {}
    rows = (
        db.query(VocabProgress)
        .filter(VocabProgress.user_id == user_id, VocabProgress.word_id.in_(word_ids))
        .all()
    )
    strength = {row.word_id: row.strength for row in rows}
    reviewed = {row.word_id: row.last_reviewed for row in rows}
    return strength, reviewed


def _batch_count(total: int) -> int:
    if total <= 0:
        return 1
    return math.ceil(total / BATCH_SIZE)


def _suggested_batch(words: list[VocabWord], strength: dict[int, int]) -> int:
    n = _batch_count(len(words))
    for index in range(n):
        chunk = words[index * BATCH_SIZE : (index + 1) * BATCH_SIZE]
        if any(strength.get(word.id, 0) < LEARNED_STRENGTH for word in chunk):
            return index + 1
    return n


def _slice_batch(words: list[VocabWord], batch_index: int) -> list[VocabWord]:
    start = (batch_index - 1) * BATCH_SIZE
    return words[start : start + BATCH_SIZE]


def _word_payload(word: VocabWord, strength: int, role: str = "new") -> dict:
    return {
        "id": word.id,
        "word": word.word,
        "transcription": word.transcription,
        "translation": word.translation,
        "part_of_speech": word.part_of_speech,
        "example": word.example,
        "example_translation": word.example_translation,
        "strength": strength,
        "role": role,
    }


def _options(correct: str, pool: list[VocabWord], attr: str, extra: list[VocabWord] | None = None, n: int = 3) -> list[str]:
    seen = {correct.strip().lower()}
    distractors: list[str] = []
    for source in (pool, extra or []):
        for word in source:
            value = getattr(word, attr)
            key = value.strip().lower()
            if key in seen:
                continue
            seen.add(key)
            distractors.append(value)
    random.shuffle(distractors)
    choices = [correct, *distractors[:n]]
    random.shuffle(choices)
    return choices[: n + 1]


def _gap_example(example: str, word: str) -> str:
    pattern = re.compile(re.escape(word), re.IGNORECASE)
    if pattern.search(example):
        return pattern.sub("______", example, count=1)
    return f"______ — {example}"


def _pick_review(
    core: list[VocabWord],
    others: list[VocabWord],
    strength: dict[int, int],
    reviewed: dict[int, datetime | None],
) -> list[VocabWord]:
    core_ids = {word.id for word in core}
    candidates = [word for word in others if word.id not in core_ids]
    weak = [word for word in candidates if 0 < strength.get(word.id, 0) < LEARNED_STRENGTH]
    weak.sort(key=lambda word: (strength.get(word.id, 0), reviewed.get(word.id) is None))
    recent = [
        word
        for word in candidates
        if word not in weak and reviewed.get(word.id) is not None
    ]
    recent.sort(key=lambda word: reviewed.get(word.id) or datetime.min.replace(tzinfo=timezone.utc), reverse=True)
    review: list[VocabWord] = []
    for word in weak + recent:
        if word not in review:
            review.append(word)
        if len(review) >= REVIEW_LIMIT:
            break
    return review


def _make_items(session: list[VocabWord], topic_words: list[VocabWord], strength: dict[int, int]) -> list[dict]:
    items: list[dict] = []
    new_words = [word for word in session if strength.get(word.id, 0) == 0][:3]
    for word in new_words:
        items.append(
            {
                "uid": f"card-{word.id}",
                "id": word.id,
                "kind": "card",
                "prompt": word.word,
                "speak": word.word,
                "transcription": word.transcription,
                "translation": word.translation,
                "part_of_speech": word.part_of_speech,
                "example": word.example,
                "example_translation": word.example_translation,
                "target": "word",
            }
        )

    kinds = ["choice_en_ru", "choice_ru_en", "type_word", "listen_pick"]
    practice_words = list(session)
    random.shuffle(practice_words)
    for index, word in enumerate(practice_words):
        kind = kinds[index % len(kinds)]
        pool = session if len(session) >= 4 else topic_words
        if kind == "choice_en_ru":
            items.append(
                {
                    "uid": f"enru-{word.id}",
                    "id": word.id,
                    "kind": kind,
                    "prompt": f"Как переводится «{word.word}»?",
                    "options": _options(word.translation, pool, "translation", topic_words),
                    "speak": word.word,
                    "target": "translation",
                }
            )
        elif kind == "choice_ru_en":
            items.append(
                {
                    "uid": f"ruen-{word.id}",
                    "id": word.id,
                    "kind": kind,
                    "prompt": f"Как по-английски: {word.translation}?",
                    "options": _options(word.word, pool, "word", topic_words),
                    "target": "word",
                }
            )
        elif kind == "type_word":
            items.append(
                {
                    "uid": f"type-{word.id}",
                    "id": word.id,
                    "kind": kind,
                    "prompt": word.translation,
                    "gap": _gap_example(word.example, word.word),
                    "hint": word.word[:1].upper(),
                    "example_translation": word.example_translation,
                    "target": "word",
                }
            )
        else:
            pick_spelling = index % 8 >= 4
            items.append(
                {
                    "uid": f"listen-{word.id}",
                    "id": word.id,
                    "kind": kind,
                    "prompt": "Прослушайте и выберите написание" if pick_spelling else "Прослушайте и выберите значение",
                    "options": _options(
                        word.word if pick_spelling else word.translation,
                        pool,
                        "word" if pick_spelling else "translation",
                        topic_words,
                    ),
                    "speak": word.word,
                    "target": "word" if pick_spelling else "translation",
                }
            )

    match_n = 5 if len(session) >= 5 else 4 if len(session) >= 4 else 0
    if match_n:
        match_words = list(session[:match_n])
        left = [{"id": word.id, "text": word.word} for word in match_words]
        right = [{"id": word.id, "text": word.translation} for word in match_words]
        random.shuffle(left)
        random.shuffle(right)
        items.append(
            {
                "uid": f"match-{match_words[0].id}",
                "id": match_words[0].id,
                "kind": "match_pairs",
                "prompt": "Соедините английские слова с переводом",
                "word_ids": [word.id for word in match_words],
                "left": left,
                "right": right,
                "target": "translation",
            }
        )
    return items


@router.get("/topics")
def list_topics(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    topics = db.query(VocabTopic).order_by(VocabTopic.sort_order).all()
    all_ids = [word.id for topic in topics for word in topic.words]
    strength, _ = _progress_maps(db, user.id, all_ids)
    result = []
    for topic in topics:
        words = sorted(topic.words, key=lambda word: word.id)
        learned = sum(1 for word in words if strength.get(word.id, 0) >= LEARNED_STRENGTH)
        result.append(
            {
                "id": topic.id,
                "slug": topic.slug,
                "title": topic.title,
                "description": topic.description,
                "level_code": topic.level_code,
                "word_count": len(words),
                "learned_count": learned,
                "batch_count": _batch_count(len(words)),
                "suggested_batch": _suggested_batch(words, strength),
            }
        )
    return result


@router.get("/topics/{slug}")
def get_topic(
    slug: str,
    batch: int | None = Query(default=None, ge=1),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    topic = db.query(VocabTopic).filter(VocabTopic.slug == slug).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Тема не найдена")
    words = _topic_words(db, topic)
    strength, _ = _progress_maps(db, user.id, [word.id for word in words])
    batch_count = _batch_count(len(words))
    suggested = _suggested_batch(words, strength)
    batch_index = min(batch or suggested, batch_count)
    batch_words = _slice_batch(words, batch_index)
    learned = sum(1 for word in words if strength.get(word.id, 0) >= LEARNED_STRENGTH)
    batch_learned = sum(1 for word in batch_words if strength.get(word.id, 0) >= LEARNED_STRENGTH)
    return {
        "id": topic.id,
        "slug": topic.slug,
        "title": topic.title,
        "description": topic.description,
        "level_code": topic.level_code,
        "word_count": len(words),
        "learned_count": learned,
        "batch_size": BATCH_SIZE,
        "batch_index": batch_index,
        "batch_count": batch_count,
        "batch_learned": batch_learned,
        "suggested_batch": suggested,
        "words": [_word_payload(word, strength.get(word.id, 0)) for word in batch_words],
    }


@router.get("/topics/{slug}/practice")
def vocab_practice(
    slug: str,
    batch: int | None = Query(default=None, ge=1),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    topic = db.query(VocabTopic).filter(VocabTopic.slug == slug).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Тема не найдена")
    words = _topic_words(db, topic)
    if not words:
        raise HTTPException(status_code=404, detail="В теме пока нет слов")
    strength, reviewed = _progress_maps(db, user.id, [word.id for word in words])
    batch_count = _batch_count(len(words))
    batch_index = min(batch or _suggested_batch(words, strength), batch_count)
    core = _slice_batch(words, batch_index)
    review = _pick_review(core, words, strength, reviewed)
    session = list(core) + [word for word in review if word not in core]
    learned = sum(1 for word in words if strength.get(word.id, 0) >= LEARNED_STRENGTH)
    return {
        "topic": {"slug": topic.slug, "title": topic.title, "level_code": topic.level_code},
        "batch_index": batch_index,
        "batch_count": batch_count,
        "batch_size": BATCH_SIZE,
        "new_count": len(core),
        "review_count": len(review),
        "word_count": len(words),
        "learned_count": learned,
        "words": [
            _word_payload(word, strength.get(word.id, 0), "review" if word in review else "new")
            for word in session
        ],
        "items": _make_items(session, words, strength),
    }


def _touch_progress(db: Session, user: User, word: VocabWord, correct: bool) -> VocabProgress:
    progress = (
        db.query(VocabProgress)
        .filter(VocabProgress.user_id == user.id, VocabProgress.word_id == word.id)
        .first()
    )
    if not progress:
        progress = VocabProgress(user_id=user.id, word_id=word.id, strength=0)
        db.add(progress)
    if correct:
        progress.strength = min(progress.strength + 1, 5)
        touch_user(db, user, 5)
    else:
        progress.strength = max(progress.strength - 1, 0)
    progress.last_reviewed = datetime.now(timezone.utc)
    return progress


@router.post("/words/{word_id}/check")
def check_word(
    word_id: int,
    payload: VocabCheckIn,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    word = db.get(VocabWord, word_id)
    if not word:
        raise HTTPException(status_code=404, detail="Слово не найдено")

    kind = payload.kind or ""
    if kind == "card":
        correct = bool(payload.remembered)
    elif kind == "match_pairs":
        correct = is_correct(payload.answer, word.translation, [word.word])
    else:
        target = payload.target or ("translation" if kind == "choice_en_ru" else "word")
        expected = word.translation if target == "translation" else word.word
        correct = is_correct(payload.answer, expected)
        if not correct and not kind:
            correct = is_correct(payload.answer, word.word, [word.translation])

    progress = _touch_progress(db, user, word, correct)
    db.commit()
    expected = word.translation if payload.target == "translation" or kind in {"choice_en_ru"} else word.word
    if kind == "card":
        expected = word.word
    return {
        "correct": correct,
        "word": word.word,
        "translation": word.translation,
        "example": word.example,
        "strength": progress.strength,
        "expected": expected if not correct else None,
    }
