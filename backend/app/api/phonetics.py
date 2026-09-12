from fastapi import APIRouter, Depends, HTTPException

from app.core.deps import get_current_user
from app.models.user import User
from app.seed.phonetics import CHART, TOPICS

router = APIRouter(prefix="/phonetics", tags=["phonetics"])


def _public_topic(topic: dict, include_body: bool = False) -> dict:
    data = {
        "slug": topic["slug"],
        "title": topic["title"],
        "description": topic["description"],
        "minutes": topic["minutes"],
    }
    if include_body:
        data["lesson"] = topic["lesson"]
    return data


@router.get("/chart")
def chart(_: User = Depends(get_current_user)):
    return CHART


@router.get("/topics")
def list_topics(_: User = Depends(get_current_user)):
    return [_public_topic(topic) for topic in TOPICS]


@router.get("/topics/{slug}")
def get_topic(slug: str, _: User = Depends(get_current_user)):
    topic = next((item for item in TOPICS if item["slug"] == slug), None)
    if not topic:
        raise HTTPException(status_code=404, detail="Тема не найдена")
    return _public_topic(topic, include_body=True)
