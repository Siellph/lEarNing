from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class StudyDeck(Base):
    """Card decks for irregular verbs, idioms, spelling exceptions, etc."""

    __tablename__ = "study_decks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    slug: Mapped[str] = mapped_column(String(160), unique=True, index=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(Text)
    kind: Mapped[str] = mapped_column(String(40), index=True)  # verbs | idioms | exceptions
    sort_order: Mapped[int] = mapped_column(Integer, default=1)

    cards = relationship("StudyCard", back_populates="deck", cascade="all, delete-orphan")


class StudyCard(Base):
    __tablename__ = "study_cards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    deck_id: Mapped[int] = mapped_column(ForeignKey("study_decks.id", ondelete="CASCADE"))
    primary_text: Mapped[str] = mapped_column(String(200))  # V1 / phrase / pattern
    secondary_text: Mapped[str] = mapped_column(String(200), default="")  # V2 / note
    tertiary_text: Mapped[str] = mapped_column(String(200), default="")  # V3
    translation: Mapped[str] = mapped_column(String(300))
    example: Mapped[str] = mapped_column(Text, default="")
    example_translation: Mapped[str] = mapped_column(Text, default="")
    category: Mapped[str] = mapped_column(String(80), default="")
    sort_order: Mapped[int] = mapped_column(Integer, default=1)

    deck = relationship("StudyDeck", back_populates="cards")
    progress = relationship("StudyProgress", back_populates="card", cascade="all, delete-orphan")


class StudyProgress(Base):
    __tablename__ = "study_progress"
    __table_args__ = (UniqueConstraint("user_id", "card_id", name="uq_user_study_card"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    card_id: Mapped[int] = mapped_column(ForeignKey("study_cards.id", ondelete="CASCADE"))
    strength: Mapped[int] = mapped_column(Integer, default=0)
    last_reviewed: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    card = relationship("StudyCard", back_populates="progress")
