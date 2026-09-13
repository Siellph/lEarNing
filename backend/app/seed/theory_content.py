"""Aggregated enriched lesson theory keyed by module slug.

Used by helpers.module() for fresh seeds and by expand.sync_lesson_theory()
to overwrite Lesson.content in already-seeded databases.
"""

from app.seed.theory_a1 import A1_THEORY
from app.seed.theory_a2 import A2_THEORY
from app.seed.theory_b1 import B1_THEORY
from app.seed.theory_b2 import B2_THEORY
from app.seed.theory_c1 import C1_THEORY
from app.seed.theory_c2 import C2_THEORY
from app.seed.theory_wo import WO_THEORY

THEORY_BY_SLUG: dict[str, dict] = {}
for pack in (
    A1_THEORY,
    A2_THEORY,
    B1_THEORY,
    B2_THEORY,
    C1_THEORY,
    C2_THEORY,
    WO_THEORY,
):
    THEORY_BY_SLUG.update(pack)
