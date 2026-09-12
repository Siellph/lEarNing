from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.settings import SiteSetting

router = APIRouter(prefix="/public", tags=["public"])


@router.get("/donation")
def public_donation(db: Session = Depends(get_db)):
    row = db.get(SiteSetting, 1)
    if not row or not row.donation_enabled or not row.donation_url.strip():
        return {"enabled": False}
    return {
        "enabled": True,
        "title": row.donation_title,
        "message": row.donation_message,
        "url": row.donation_url.strip(),
        "button": row.donation_button or "Оставить чаевые",
    }
