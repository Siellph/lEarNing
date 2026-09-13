"""Aggregated enriched lesson theory keyed by module slug.

Used by helpers.module() for fresh seeds and by expand.sync_lesson_theory()
to overwrite Lesson.content in already-seeded databases.

B2–C2 keep their in-file lessons (already dense); overrides focus on thinner
A1–B1 and word-order modules.
"""

from app.seed.theory_a1 import A1_THEORY
from app.seed.theory_a2 import A2_THEORY
from app.seed.theory_b1 import B1_THEORY
from app.seed.theory_wo import WO_THEORY

THEORY_BY_SLUG: dict[str, dict] = {}
for pack in (A1_THEORY, A2_THEORY, B1_THEORY, WO_THEORY):
    THEORY_BY_SLUG.update(pack)
