from sqlalchemy import Boolean, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class SiteSetting(Base):
    __tablename__ = "site_settings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    donation_enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    donation_title: Mapped[str] = mapped_column(String(200), default="Сайт оказался полезным?")
    donation_message: Mapped[str] = mapped_column(
        Text,
        default="Если lEarNinG помогает учить ENG, можно оставить чаевые — это поддерживает развитие курса.",
    )
    donation_url: Mapped[str] = mapped_column(String(500), default="")
    donation_button: Mapped[str] = mapped_column(String(80), default="Оставить чаевые")
    email_verification_required: Mapped[bool] = mapped_column(Boolean, default=True)
