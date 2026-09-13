import math
import random
from collections import defaultdict
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

# Four-way mastery bits — word is learned when mastery == LEARNED_MASTERY.
MASTERY_BITS = {
    "choice_en_ru": 1,
    "type_en_ru": 2,
    "choice_ru_en": 4,
    "type_ru_en": 8,
}
# Legacy aliases from the previous practice pack.
MASTERY_BITS["type_word"] = MASTERY_BITS["type_ru_en"]
LEARNED_MASTERY = 15
TASK_KINDS = ("choice_en_ru", "type_en_ru", "choice_ru_en", "type_ru_en")


def _topic_words(db: Session, topic: VocabTopic) -> list[VocabWord]:
    return db.query(VocabWord).filter(VocabWord.topic_id == topic.id).order_by(VocabWord.id).all()


def _progress_maps(
    db: Session, user_id: int, word_ids: list[int]
) -> tuple[dict[int, int], dict[int, int], dict[int, datetime | None]]:
    if not word_ids:
        return {}, {}, {}
    rows = (
        db.query(VocabProgress)
        .filter(VocabProgress.user_id == user_id, VocabProgress.word_id.in_(word_ids))
        .all()
    )
    strength = {row.word_id: row.strength for row in rows}
    mastery = {row.word_id: int(getattr(row, "mastery", 0) or 0) for row in rows}
    reviewed = {row.word_id: row.last_reviewed for row in rows}
    return strength, mastery, reviewed


def _batch_count(total: int) -> int:
    if total <= 0:
        return 1
    return math.ceil(total / BATCH_SIZE)


def _is_learned(mastery_value: int) -> bool:
    return mastery_value >= LEARNED_MASTERY


def _mastery_count(mastery_value: int) -> int:
    return bin(mastery_value & LEARNED_MASTERY).count("1")


def _suggested_batch(words: list[VocabWord], mastery: dict[int, int]) -> int:
    n = _batch_count(len(words))
    for index in range(n):
        chunk = words[index * BATCH_SIZE : (index + 1) * BATCH_SIZE]
        if any(not _is_learned(mastery.get(word.id, 0)) for word in chunk):
            return index + 1
    return n


def _slice_batch(words: list[VocabWord], batch_index: int) -> list[VocabWord]:
    start = (batch_index - 1) * BATCH_SIZE
    return words[start : start + BATCH_SIZE]


def _word_payload(word: VocabWord, strength: int, mastery_value: int, role: str = "new") -> dict:
    return {
        "id": word.id,
        "word": word.word,
        "transcription": word.transcription,
        "translation": word.translation,
        "part_of_speech": word.part_of_speech,
        "example": word.example,
        "example_translation": word.example_translation,
        "strength": strength,
        "mastery": mastery_value,
        "mastery_count": _mastery_count(mastery_value),
        "learned": _is_learned(mastery_value),
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


def _build_task(word: VocabWord, kind: str, pool: list[VocabWord], topic_words: list[VocabWord]) -> dict:
    if kind == "choice_en_ru":
        return {
            "uid": f"enru-{word.id}",
            "id": word.id,
            "kind": kind,
            "prompt": f"Как переводится «{word.word}»?",
            "options": _options(word.translation, pool, "translation", topic_words),
            "speak": word.word,
            "target": "translation",
        }
    if kind == "type_en_ru":
        return {
            "uid": f"typeru-{word.id}",
            "id": word.id,
            "kind": kind,
            "prompt": f"Напишите перевод слова «{word.word}»",
            "speak": word.word,
            "hint": word.translation[:1],
            "target": "translation",
        }
    if kind == "choice_ru_en":
        return {
            "uid": f"ruen-{word.id}",
            "id": word.id,
            "kind": kind,
            "prompt": f"Как по-английски: «{word.translation}»?",
            "options": _options(word.word, pool, "word", topic_words),
            "target": "word",
        }
    # type_ru_en
    return {
        "uid": f"typeen-{word.id}",
        "id": word.id,
        "kind": kind,
        "prompt": f"Напишите по-английски: «{word.translation}»",
        "hint": word.word[:1].upper(),
        "example": word.example,
        "example_translation": word.example_translation,
        "target": "word",
    }


def _interleave_shuffle(items: list[dict]) -> list[dict]:
    """Shuffle tasks preferring not to show the same word twice in a row."""
    by_word: dict[int, list[dict]] = defaultdict(list)
    for item in items:
        by_word[item["id"]].append(item)
    for bucket in by_word.values():
        random.shuffle(bucket)

    word_ids = list(by_word.keys())
    random.shuffle(word_ids)
    result: list[dict] = []
    last_id: int | None = None
    remaining = sum(len(bucket) for bucket in by_word.values())
    while remaining:
        candidates = [wid for wid in word_ids if by_word[wid] and wid != last_id]
        if not candidates:
            candidates = [wid for wid in word_ids if by_word[wid]]
        wid = random.choice(candidates)
        result.append(by_word[wid].pop())
        last_id = wid
        remaining -= 1
    return result


def _make_items(
    batch_words: list[VocabWord],
    topic_words: list[VocabWord],
    mastery: dict[int, int],
) -> list[dict]:
    """One pending task per missing mastery bit for words not yet fully learned.

    Choice (MCQ) tasks run first, then typing — reduces keyboard open/close thrash on mobile.
    Within each group, tasks are interleaved so the same word rarely appears twice in a row.
    """
    pending: list[dict] = []
    pool = batch_words if len(batch_words) >= 4 else topic_words
    for word in batch_words:
        flags = mastery.get(word.id, 0)
        if _is_learned(flags):
            continue
        missing = [kind for kind in TASK_KINDS if not (flags & MASTERY_BITS[kind])]
        random.shuffle(missing)
        for kind in missing:
            pending.append(_build_task(word, kind, pool, topic_words))
    choice = [item for item in pending if str(item.get("kind", "")).startswith("choice_")]
    typing = [item for item in pending if not str(item.get("kind", "")).startswith("choice_")]
    return _interleave_shuffle(choice) + _interleave_shuffle(typing)


@router.get("/topics")
def list_topics(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    topics = db.query(VocabTopic).order_by(VocabTopic.sort_order).all()
    all_ids = [word.id for topic in topics for word in topic.words]
    _, mastery, _ = _progress_maps(db, user.id, all_ids)
    result = []
    for topic in topics:
        words = sorted(topic.words, key=lambda word: word.id)
        learned = sum(1 for word in words if _is_learned(mastery.get(word.id, 0)))
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
                "suggested_batch": _suggested_batch(words, mastery),
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
    strength, mastery, _ = _progress_maps(db, user.id, [word.id for word in words])
    batch_count = _batch_count(len(words))
    suggested = _suggested_batch(words, mastery)
    batch_index = min(batch or suggested, batch_count)
    batch_words = _slice_batch(words, batch_index)
    learned = sum(1 for word in words if _is_learned(mastery.get(word.id, 0)))
    batch_learned = sum(1 for word in batch_words if _is_learned(mastery.get(word.id, 0)))
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
        "words": [
            _word_payload(word, strength.get(word.id, 0), mastery.get(word.id, 0)) for word in batch_words
        ],
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
    strength, mastery, _ = _progress_maps(db, user.id, [word.id for word in words])
    batch_count = _batch_count(len(words))
    batch_index = min(batch or _suggested_batch(words, mastery), batch_count)
    core = _slice_batch(words, batch_index)
    pending_words = [word for word in core if not _is_learned(mastery.get(word.id, 0))]
    items = _make_items(pending_words, words, mastery)
    learned = sum(1 for word in words if _is_learned(mastery.get(word.id, 0)))
    batch_learned = sum(1 for word in core if _is_learned(mastery.get(word.id, 0)))
    return {
        "topic": {"slug": topic.slug, "title": topic.title, "level_code": topic.level_code},
        "batch_index": batch_index,
        "batch_count": batch_count,
        "batch_size": BATCH_SIZE,
        "new_count": len(pending_words),
        "review_count": 0,
        "word_count": len(words),
        "learned_count": learned,
        "batch_learned": batch_learned,
        "batch_word_count": len(core),
        "pending_tasks": len(items),
        "words": [
            _word_payload(word, strength.get(word.id, 0), mastery.get(word.id, 0), "new") for word in pending_words
        ],
        "items": items,
    }


def _touch_progress(
    db: Session,
    user: User,
    word: VocabWord,
    correct: bool,
    kind: str,
) -> VocabProgress:
    progress = (
        db.query(VocabProgress)
        .filter(VocabProgress.user_id == user.id, VocabProgress.word_id == word.id)
        .first()
    )
    if not progress:
        progress = VocabProgress(user_id=user.id, word_id=word.id, strength=0, mastery=0)
        db.add(progress)

    bit = MASTERY_BITS.get(kind, 0)
    if correct and bit:
        before = int(progress.mastery or 0)
        if not (before & bit):
            progress.mastery = before | bit
            touch_user(db, user, 5)
        progress.strength = _mastery_count(progress.mastery)
    # Wrong answers do not clear mastery bits; the facet stays pending for a later pass.
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
    target = payload.target or (
        "translation" if kind in {"choice_en_ru", "type_en_ru"} else "word"
    )
    expected = word.translation if target == "translation" else word.word
    correct = is_correct(payload.answer, expected)
    if not correct and not kind:
        correct = is_correct(payload.answer, word.word, [word.translation])

    progress = _touch_progress(db, user, word, correct, kind)
    db.commit()
    mastery_value = int(progress.mastery or 0)
    return {
        "correct": correct,
        "word": word.word,
        "translation": word.translation,
        "example": word.example,
        "strength": progress.strength,
        "mastery": mastery_value,
        "mastery_count": _mastery_count(mastery_value),
        "learned": _is_learned(mastery_value),
        "expected": expected if not correct else None,
    }
