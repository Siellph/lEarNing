SOURCES = [
    "CEFR / Cambridge English — grammar syllabus",
    "British Council LearnEnglish — Grammar",
    "Oxford Practice Grammar — topic map",
    "English Grammar in Use (Murphy) — topic coverage",
]


def mc(
    prompt: str,
    options: list[str],
    answer: str,
    explanation: str,
    accepted: list[str] | None = None,
) -> dict:
    return {
        "kind": "multiple_choice",
        "prompt": prompt,
        "options": options,
        "answer": answer,
        "accepted": accepted or [],
        "explanation": explanation,
    }


def fill(prompt: str, answer: str, explanation: str, accepted: list[str] | None = None) -> dict:
    return {
        "kind": "fill_blank",
        "prompt": prompt,
        "answer": answer,
        "accepted": accepted or [],
        "explanation": explanation,
    }


def xf(prompt: str, answer: str, explanation: str, accepted: list[str] | None = None) -> dict:
    return {
        "kind": "transform",
        "prompt": prompt,
        "answer": answer,
        "accepted": accepted or [],
        "explanation": explanation,
    }


def err(prompt: str, answer: str, explanation: str, accepted: list[str] | None = None) -> dict:
    return {
        "kind": "error_correction",
        "prompt": prompt,
        "answer": answer,
        "accepted": accepted or [],
        "explanation": explanation,
    }


def order(prompt: str, answer: str, explanation: str, accepted: list[str] | None = None) -> dict:
    return {
        "kind": "order",
        "prompt": prompt,
        "answer": answer,
        "accepted": accepted or [],
        "explanation": explanation,
    }


def match(prompt: str, options: list[str], answer: str, explanation: str) -> dict:
    """Match pairs: options are left sides; answer is 'A=1;B=2' style or the correct pairing string."""
    return {
        "kind": "match",
        "prompt": prompt,
        "options": options,
        "answer": answer,
        "accepted": [],
        "explanation": explanation,
    }


def ex(en: str, ru: str) -> dict:
    return {"en": en, "ru": ru}


def rule(title: str, body: str, examples: list[dict]) -> dict:
    return {"title": title, "body": body, "examples": examples}


def lesson(
    intro: str,
    rules: list[dict],
    watch_out: list[str] | None = None,
    remember: str = "",
    compare: list[dict] | None = None,
    articulation: str = "",
    contrast: str = "",
    tips: list[str] | None = None,
) -> dict:
    return {
        "intro": intro,
        "rules": rules,
        "compare": compare or [],
        "watch_out": watch_out or [],
        "remember": remember,
        "articulation": articulation,
        "contrast": contrast,
        "tips": tips or [],
    }


def module(
    slug: str,
    title: str,
    description: str,
    minutes: int,
    lesson_title: str,
    content: dict,
    exercises: list[dict],
    test: list[dict],
) -> dict:
    return {
        "slug": slug,
        "title": title,
        "description": description,
        "minutes": minutes,
        "sources": SOURCES,
        "lesson": {"title": lesson_title, "content": content},
        "exercises": exercises,
        "test": test,
    }
