from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class VocabTopic(Base):
    __tablename__ = "vocab_topics"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    slug: Mapped[str] = mapped_column(String(160), unique=True, index=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(Text)
    level_code: Mapped[str] = mapped_column(String(8))
    sort_order: Mapped[int] = mapped_column(Integer)

    words = relationship("VocabWord", back_populates="topic", cascade="all, delete-orphan")


class VocabWord(Base):
    __tablename__ = "vocab_words"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    topic_id: Mapped[int] = mapped_column(ForeignKey("vocab_topics.id", ondelete="CASCADE"))
    word: Mapped[str] = mapped_column(String(120))
    transcription: Mapped[str] = mapped_column(String(120))
    translation: Mapped[str] = mapped_column(String(200))
    part_of_speech: Mapped[str] = mapped_column(String(40))
    example: Mapped[str] = mapped_column(Text)
    example_translation: Mapped[str] = mapped_column(Text)

    topic = relationship("VocabTopic", back_populates="words")
    progress = relationship("VocabProgress", back_populates="word", cascade="all, delete-orphan")


class VocabProgress(Base):
    __tablename__ = "vocab_progress"
    __table_args__ = (UniqueConstraint("user_id", "word_id", name="uq_user_word"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    word_id: Mapped[int] = mapped_column(ForeignKey("vocab_words.id", ondelete="CASCADE"))
    strength: Mapped[int] = mapped_column(Integer, default=0)
    last_reviewed: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="vocab_progress")
    word = relationship("VocabWord", back_populates="progress")
