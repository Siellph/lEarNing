from sqlalchemy import ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class GrammarLevel(Base):
    __tablename__ = "grammar_levels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String(8), unique=True, index=True)
    title: Mapped[str] = mapped_column(String(120))
    subtitle: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    sort_order: Mapped[int] = mapped_column(Integer)

    modules = relationship("GrammarModule", back_populates="level", cascade="all, delete-orphan")
    exams = relationship("Exam", back_populates="level", cascade="all, delete-orphan")


class GrammarModule(Base):
    __tablename__ = "grammar_modules"
    __table_args__ = (UniqueConstraint("slug", name="uq_module_slug"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    level_id: Mapped[int] = mapped_column(ForeignKey("grammar_levels.id", ondelete="CASCADE"))
    slug: Mapped[str] = mapped_column(String(160), index=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(Text)
    sort_order: Mapped[int] = mapped_column(Integer)
    estimated_minutes: Mapped[int] = mapped_column(Integer, default=20)
    sources: Mapped[list] = mapped_column(JSONB, default=list)

    level = relationship("GrammarLevel", back_populates="modules")
    lessons = relationship("Lesson", back_populates="module", cascade="all, delete-orphan")
    exercises = relationship("Exercise", back_populates="module", cascade="all, delete-orphan")
    test = relationship("ModuleTest", back_populates="module", uselist=False, cascade="all, delete-orphan")
    progress = relationship("ModuleProgress", back_populates="module", cascade="all, delete-orphan")


class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    module_id: Mapped[int] = mapped_column(ForeignKey("grammar_modules.id", ondelete="CASCADE"))
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[dict] = mapped_column(JSONB)
    sort_order: Mapped[int] = mapped_column(Integer, default=1)

    module = relationship("GrammarModule", back_populates="lessons")
    exercises = relationship("Exercise", back_populates="lesson")


class Exercise(Base):
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    module_id: Mapped[int] = mapped_column(ForeignKey("grammar_modules.id", ondelete="CASCADE"))
    lesson_id: Mapped[int | None] = mapped_column(ForeignKey("lessons.id", ondelete="SET NULL"), nullable=True)
    kind: Mapped[str] = mapped_column(String(40))
    prompt: Mapped[str] = mapped_column(Text)
    options: Mapped[list | None] = mapped_column(JSONB, nullable=True)
    answer: Mapped[str] = mapped_column(Text)
    accepted: Mapped[list | None] = mapped_column(JSONB, nullable=True)
    explanation: Mapped[str] = mapped_column(Text)
    sort_order: Mapped[int] = mapped_column(Integer, default=1)
    xp: Mapped[int] = mapped_column(Integer, default=10)

    module = relationship("GrammarModule", back_populates="exercises")
    lesson = relationship("Lesson", back_populates="exercises")
    attempts = relationship("ExerciseAttempt", back_populates="exercise", cascade="all, delete-orphan")


class ModuleTest(Base):
    __tablename__ = "module_tests"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    module_id: Mapped[int] = mapped_column(ForeignKey("grammar_modules.id", ondelete="CASCADE"), unique=True)
    title: Mapped[str] = mapped_column(String(200))
    time_limit_sec: Mapped[int] = mapped_column(Integer, default=600)
    passing_score: Mapped[int] = mapped_column(Integer, default=70)

    module = relationship("GrammarModule", back_populates="test")
    questions = relationship("TestQuestion", back_populates="test", cascade="all, delete-orphan")
    attempts = relationship("TestAttempt", back_populates="test", cascade="all, delete-orphan")


class TestQuestion(Base):
    __tablename__ = "test_questions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    test_id: Mapped[int] = mapped_column(ForeignKey("module_tests.id", ondelete="CASCADE"))
    kind: Mapped[str] = mapped_column(String(40))
    prompt: Mapped[str] = mapped_column(Text)
    options: Mapped[list | None] = mapped_column(JSONB, nullable=True)
    answer: Mapped[str] = mapped_column(Text)
    accepted: Mapped[list | None] = mapped_column(JSONB, nullable=True)
    explanation: Mapped[str] = mapped_column(Text)
    sort_order: Mapped[int] = mapped_column(Integer, default=1)

    test = relationship("ModuleTest", back_populates="questions")


class Exam(Base):
    __tablename__ = "exams"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    level_id: Mapped[int] = mapped_column(ForeignKey("grammar_levels.id", ondelete="CASCADE"))
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(Text)
    time_limit_sec: Mapped[int] = mapped_column(Integer, default=1800)
    passing_score: Mapped[int] = mapped_column(Integer, default=75)

    level = relationship("GrammarLevel", back_populates="exams")
    questions = relationship("ExamQuestion", back_populates="exam", cascade="all, delete-orphan")
    attempts = relationship("ExamAttempt", back_populates="exam", cascade="all, delete-orphan")


class ExamQuestion(Base):
    __tablename__ = "exam_questions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    exam_id: Mapped[int] = mapped_column(ForeignKey("exams.id", ondelete="CASCADE"))
    kind: Mapped[str] = mapped_column(String(40))
    prompt: Mapped[str] = mapped_column(Text)
    options: Mapped[list | None] = mapped_column(JSONB, nullable=True)
    answer: Mapped[str] = mapped_column(Text)
    accepted: Mapped[list | None] = mapped_column(JSONB, nullable=True)
    explanation: Mapped[str] = mapped_column(Text)
    sort_order: Mapped[int] = mapped_column(Integer, default=1)

    exam = relationship("Exam", back_populates="questions")
