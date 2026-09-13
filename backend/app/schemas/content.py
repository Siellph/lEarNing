from pydantic import BaseModel, Field


class LessonContent(BaseModel):
    """Lesson theory payload.

    Each rule may include optional structured blocks (ignored if absent):
    - tables: [{headers: [...], rows: [[...], ...]}]
    - callouts: [{tone: key|warn|tip, text}]
    - pairs: [{wrong, right, note?}]
    Body text may use **…** for emphasis (frontend-only; not HTML).
    """

    intro: str
    rules: list[dict]
    compare: list[dict] = []
    watch_out: list[str] = []
    remember: str = ""
    articulation: str = ""
    contrast: str = ""
    tips: list[str] = []


class LessonIn(BaseModel):
    title: str
    content: dict
    sort_order: int = 1


class ExerciseIn(BaseModel):
    kind: str
    prompt: str
    options: list[str] | None = None
    answer: str
    accepted: list[str] | None = None
    explanation: str
    sort_order: int = 1
    xp: int = 10
    lesson_id: int | None = None


class ModuleIn(BaseModel):
    level_id: int
    slug: str
    title: str
    description: str
    sort_order: int
    estimated_minutes: int = 20
    sources: list[str] = []


class ModuleUpdateIn(BaseModel):
    title: str | None = None
    description: str | None = None
    sort_order: int | None = None
    estimated_minutes: int | None = None
    sources: list[str] | None = None


class VocabTopicIn(BaseModel):
    slug: str
    title: str
    description: str
    level_code: str
    sort_order: int = 99


class VocabTopicUpdateIn(BaseModel):
    slug: str | None = None
    title: str | None = None
    description: str | None = None
    level_code: str | None = None
    sort_order: int | None = None


class VocabWordIn(BaseModel):
    topic_id: int
    word: str
    transcription: str = ""
    translation: str
    part_of_speech: str = "noun"
    example: str
    example_translation: str


class VocabWordUpdateIn(BaseModel):
    topic_id: int | None = None
    word: str | None = None
    transcription: str | None = None
    translation: str | None = None
    part_of_speech: str | None = None
    example: str | None = None
    example_translation: str | None = None


class AnswerIn(BaseModel):
    answer: str = Field(min_length=1, max_length=500)


class VocabCheckIn(BaseModel):
    answer: str = ""
    kind: str = ""
    target: str | None = None
    remembered: bool | None = None


class TestSubmitIn(BaseModel):
    answers: dict[str, str]


class ExamSubmitIn(BaseModel):
    answers: dict[str, str]


class AttemptAnswersIn(BaseModel):
    answers: dict[str, str]


class AttemptSubmitIn(BaseModel):
    answers: dict[str, str] | None = None


class QuestionIn(BaseModel):
    kind: str
    prompt: str
    options: list[str] | None = None
    answer: str
    accepted: list[str] | None = None
    explanation: str = "Проверьте форму и правило."
    sort_order: int = 1


class DonationIn(BaseModel):
    donation_enabled: bool = False
    donation_title: str = Field(default="Сайт оказался полезным?", max_length=200)
    donation_message: str = Field(default="", max_length=1000)
    donation_url: str = Field(default="", max_length=500)
    donation_button: str = Field(default="Оставить чаевые", max_length=80)


class ExerciseUpdateIn(BaseModel):
    kind: str | None = None
    prompt: str | None = None
    options: list[str] | None = None
    answer: str | None = None
    accepted: list[str] | None = None
    explanation: str | None = None
    sort_order: int | None = None
    xp: int | None = None


class QuestionUpdateIn(BaseModel):
    kind: str | None = None
    prompt: str | None = None
    options: list[str] | None = None
    answer: str | None = None
    accepted: list[str] | None = None
    explanation: str | None = None
    sort_order: int | None = None


class RegistrationSettingsIn(BaseModel):
    email_verification_required: bool = True


class StudyCheckIn(BaseModel):
    answer: str = ""
    kind: str = ""
    target: str | None = None
    accepted: list[str] | None = None
    remembered: bool | None = None


class SkillCheckIn(BaseModel):
    answer: str = ""
    kind: str = ""


class StudyCardIn(BaseModel):
    deck_id: int
    primary_text: str
    secondary_text: str = ""
    tertiary_text: str = ""
    translation: str
    example: str = ""
    example_translation: str = ""
    category: str = ""
    sort_order: int = 1


class StudyCardUpdateIn(BaseModel):
    primary_text: str | None = None
    secondary_text: str | None = None
    tertiary_text: str | None = None
    translation: str | None = None
    example: str | None = None
    example_translation: str | None = None
    category: str | None = None
    sort_order: int | None = None


class StudyDeckIn(BaseModel):
    slug: str
    title: str
    description: str = ""
    kind: str  # verbs | idioms | exceptions
    sort_order: int = 99


class StudyDeckUpdateIn(BaseModel):
    slug: str | None = None
    title: str | None = None
    description: str | None = None
    kind: str | None = None
    sort_order: int | None = None


class SkillItemIn(BaseModel):
    slug: str
    title: str
    description: str = ""
    kind: str  # reading | listening | dialogue
    level_code: str = "A1"
    body: str = ""
    lines: list = []
    keywords: list = []
    sort_order: int = 99


class SkillItemUpdateIn(BaseModel):
    slug: str | None = None
    title: str | None = None
    description: str | None = None
    kind: str | None = None
    level_code: str | None = None
    body: str | None = None
    lines: list | None = None
    keywords: list | None = None
    sort_order: int | None = None


class SkillQuestionIn(BaseModel):
    item_id: int
    kind: str  # choice | dictation | fill_gap
    prompt: str
    options: list[str] | None = None
    answer: str
    accepted: list[str] | None = None
    speak: str = ""
    explanation: str = ""
    sort_order: int = 1


class SkillQuestionUpdateIn(BaseModel):
    kind: str | None = None
    prompt: str | None = None
    options: list[str] | None = None
    answer: str | None = None
    accepted: list[str] | None = None
    speak: str | None = None
    explanation: str | None = None
    sort_order: int | None = None
