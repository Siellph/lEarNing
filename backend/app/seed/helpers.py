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
    """Match pairs for UI: always expose {left, right}; answer stays 'A=B; C=D'."""
    from app.services.match_format import normalize_match_payload

    sides, aligned = normalize_match_payload(list(options), answer)
    return {
        "kind": "match",
        "prompt": prompt,
        "options": sides,
        "answer": aligned,
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
    # Lazy import avoids circular dependency with theory_* packs.
    from app.seed.theory_content import THEORY_BY_SLUG

    # A1–B1 / word-order overrides are authored as replacements; always prefer them.
    lesson_content = THEORY_BY_SLUG.get(slug, content)
    return {
        "slug": slug,
        "title": title,
        "description": description,
        "minutes": minutes,
        "sources": SOURCES,
        "lesson": {"title": lesson_title, "content": lesson_content},
        "exercises": exercises,
        "test": test,
    }
