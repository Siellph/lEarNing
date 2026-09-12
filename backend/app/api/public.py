from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import get_db
from app.models.settings import SiteSetting

router = APIRouter(prefix="/public", tags=["public"])


@router.get("/donation")
def public_donation(db: Session = Depends(get_db)):
    row = db.get(SiteSetting, 1)
    url = ((row.donation_url if row else "") or settings.DONATION_URL).strip()
    enabled = bool((row.donation_enabled if row else False) or settings.DONATION_ENABLED) and bool(url)
    if not enabled:
        return {"enabled": False}
    return {
        "enabled": True,
        "title": (row.donation_title if row and row.donation_title else None) or settings.DONATION_TITLE or "Сайт оказался полезным?",
        "message": (row.donation_message if row and row.donation_message else None)
        or settings.DONATION_MESSAGE
        or "Если lEarNing помогает учить EN, можно оставить чаевые — это поддерживает развитие курса.",
        "url": url,
        "button": (row.donation_button if row and row.donation_button else None) or settings.DONATION_BUTTON or "Оставить чаевые",
    }
