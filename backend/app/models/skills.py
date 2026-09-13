"""Graded reading, listening clips, and mini-dialogues."""

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class SkillItem(Base):
    """One reading passage, listening clip, or dialogue scene."""

    __tablename__ = "skill_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    slug: Mapped[str] = mapped_column(String(160), unique=True, index=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(Text, default="")
    kind: Mapped[str] = mapped_column(String(40), index=True)  # reading | listening | dialogue
    level_code: Mapped[str] = mapped_column(String(8), default="A1")
    body: Mapped[str] = mapped_column(Text, default="")  # passage / transcript
    lines: Mapped[list] = mapped_column(JSONB, default=list)  # dialogue turns
    keywords: Mapped[list] = mapped_column(JSONB, default=list)  # [{en, ru}]
    sort_order: Mapped[int] = mapped_column(Integer, default=1)

    questions = relationship("SkillQuestion", back_populates="item", cascade="all, delete-orphan")
    progress = relationship("SkillProgress", back_populates="item", cascade="all, delete-orphan")


class SkillQuestion(Base):
    __tablename__ = "skill_questions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("skill_items.id", ondelete="CASCADE"))
    kind: Mapped[str] = mapped_column(String(40))  # choice | dictation | fill_gap
    prompt: Mapped[str] = mapped_column(Text)
    options: Mapped[list | None] = mapped_column(JSONB, nullable=True)
    answer: Mapped[str] = mapped_column(Text)
    accepted: Mapped[list | None] = mapped_column(JSONB, nullable=True)
    speak: Mapped[str] = mapped_column(Text, default="")  # TTS override (dictation snippets)
    explanation: Mapped[str] = mapped_column(Text, default="")
    sort_order: Mapped[int] = mapped_column(Integer, default=1)

    item = relationship("SkillItem", back_populates="questions")


class SkillProgress(Base):
    __tablename__ = "skill_progress"
    __table_args__ = (UniqueConstraint("user_id", "item_id", name="uq_user_skill_item"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    item_id: Mapped[int] = mapped_column(ForeignKey("skill_items.id", ondelete="CASCADE"))
    strength: Mapped[int] = mapped_column(Integer, default=0)
    last_reviewed: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    item = relationship("SkillItem", back_populates="progress")
