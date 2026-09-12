import re
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.progress import ModuleProgress
from app.models.user import User


def normalize(value: str) -> str:
    text = value.strip().lower()
    text = text.replace("’", "'").replace("`", "'")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[.!?]+$", "", text)
    return text


def is_correct(given: str, answer: str, accepted: list[str] | None = None) -> bool:
    candidates = [answer, *(accepted or [])]
    given_n = normalize(given)
    return any(given_n == normalize(item) for item in candidates)


def percent(correct: int, total: int) -> int:
    if total <= 0:
        return 0
    return round(correct * 100 / total)


def touch_user(db: Session, user: User, xp: int = 0) -> None:
    now = datetime.now(timezone.utc)
    if user.last_activity:
        last = user.last_activity
        if last.tzinfo is None:
            last = last.replace(tzinfo=timezone.utc)
        delta = now.date() - last.date()
        if delta.days == 1:
            user.streak += 1
        elif delta.days > 1:
            user.streak = 1
    else:
        user.streak = max(user.streak, 1)
    user.last_activity = now
    user.xp += xp
    db.add(user)


def get_or_create_progress(db: Session, user_id: int, module_id: int) -> ModuleProgress:
    progress = (
        db.query(ModuleProgress)
        .filter(ModuleProgress.user_id == user_id, ModuleProgress.module_id == module_id)
        .first()
    )
    if not progress:
        progress = ModuleProgress(user_id=user_id, module_id=module_id, status="in_progress")
        db.add(progress)
        db.flush()
    return progress


def refresh_module_status(progress: ModuleProgress) -> None:
    if progress.test_score is not None and progress.test_score >= 70:
        progress.status = "completed"
    elif progress.lesson_done or progress.practice_score > 0:
        progress.status = "in_progress"
    else:
        progress.status = "not_started"
