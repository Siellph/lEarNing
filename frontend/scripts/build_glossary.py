#!/usr/bin/env python3
"""Merge harvested example vocabulary into frontend/src/lib/glossary.ts.

Usage:
  python frontend/scripts/build_glossary.py

Reads existing GLOSSARY entries, adds translations from example_glosses.json
(for any harvested word still missing), and rewrites glossary.ts.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GLOSSARY_TS = ROOT / "frontend" / "src" / "lib" / "glossary.ts"
EXTRA_JSON = Path(__file__).resolve().parent / "example_glosses.json"

# Reuse harvest helpers
sys.path.insert(0, str(Path(__file__).resolve().parent))
from harvest_glossary import collect_sentences, words_from_sentences, load_glossary_keys  # noqa: E402

ENTRY_RE = re.compile(
    r'^\s*([a-z][a-z0-9\']*)\s*:\s*"((?:\\.|[^"\\])*)"\s*,?\s*$',
    re.M,
)


def parse_existing() -> dict[str, str]:
    text = GLOSSARY_TS.read_text(encoding="utf-8")
    out: dict[str, str] = {}
    for m in ENTRY_RE.finditer(text):
        key, val = m.group(1), m.group(2)
        out[key] = bytes(val, "utf-8").decode("unicode_escape") if "\\" in val else val
        # Prefer literal_eval-style for escapes
        try:
            import ast

            out[key] = ast.literal_eval('"' + val + '"')
        except Exception:
            out[key] = val
    return out


def ts_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def render(glossary: dict[str, str]) -> str:
    lines = [
        "/**",
        " * Offline EN→RU glosses for hover tips on **lesson example** English only",
        " * (`LessonView` examples / compare rows — not quiz prompts or app chrome).",
        " *",
        " * Regenerated / extended via `frontend/scripts/build_glossary.py`",
        " * from vocabulary harvested in lesson seeds (`ex(en, ru)`, compare left/right).",
        " */",
        "export const GLOSSARY: Record<string, string> = {",
    ]
    for key in sorted(glossary.keys()):
        lines.append(f'  {key}: "{ts_escape(glossary[key])}",')
    lines.append("};")
    lines.append("")
    lines.append(
        """\
/** Normalize a surface token to a glossary key (offline lookup only). */
export function lookupGloss(raw: string): string | null {
  const stripped = raw
    .normalize("NFD")
    .replace(/[\\u0300-\\u036f]/g, "")
    .toLowerCase()
    .replace(/^[^a-z']+|[^a-z']+$/gi, "");

  if (!stripped) return null;

  const direct = GLOSSARY[stripped];
  if (direct) return direct;

  // Possessive: teacher's → teacher
  if (stripped.endsWith("'s")) {
    const base = stripped.slice(0, -2);
    if (GLOSSARY[base]) return GLOSSARY[base];
  }

  // Negatives: doesn't → does + not; won't/can't special-cased
  if (stripped.endsWith("n't")) {
    const head = stripped.slice(0, -3);
    const mapped =
      head === "wo" ? "will" : head === "ca" ? "can" : head === "sha" ? "shall" : head;
    const g = GLOSSARY[mapped];
    const notG = GLOSSARY.not || "не";
    if (g) return `${g} + ${notG}`;
    return notG;
  }

  // Common clitic contractions
  const clitics: Record<string, string> = {
    "i'm": "i",
    "i've": "i",
    "i'll": "i",
    "i'd": "i",
    "you're": "you",
    "you've": "you",
    "you'll": "you",
    "you'd": "you",
    "he's": "he",
    "she's": "she",
    "it's": "it",
    "we're": "we",
    "we've": "we",
    "we'll": "we",
    "we'd": "we",
    "they're": "they",
    "they've": "they",
    "they'll": "they",
    "they'd": "they",
    "that's": "that",
    "there's": "there",
    "here's": "here",
    "who's": "who",
    "what's": "what",
    "where's": "where",
    "let's": "let",
  };
  const via = clitics[stripped];
  if (via && GLOSSARY[via]) return GLOSSARY[via];

  return null;
}
"""
    )
    return "\n".join(lines)


def main() -> int:
    existing = parse_existing()
    extra: dict[str, str] = {}
    if EXTRA_JSON.exists():
        extra = json.loads(EXTRA_JSON.read_text(encoding="utf-8"))

    words = words_from_sentences(collect_sentences())
    from harvest_glossary import IGNORE

    skip = set(IGNORE)
    missing = sorted(
        w for w in words if len(w) >= 2 and w not in existing and w not in skip and w not in extra
    )

    merged = dict(existing)
    merged.update(extra)
    merged.setdefault("math", "математика")
    merged.setdefault("maths", "математика")
    merged.setdefault("station", "вокзал / станция")

    still = [w for w in words if len(w) >= 2 and w not in merged and w not in skip]
    if still:
        print(f"WARNING: {len(still)} words still lack glosses:", file=sys.stderr)
        for w in still[:40]:
            print(f"  {w}", file=sys.stderr)
        if len(still) > 40:
            print(f"  ... +{len(still) - 40} more", file=sys.stderr)

    GLOSSARY_TS.write_text(render(merged), encoding="utf-8")
    print(f"Wrote {GLOSSARY_TS.relative_to(ROOT)} with {len(merged)} entries")
    print(f"Harvested words covered: {sum(1 for w in words if len(w) >= 2 and w in merged)} / {sum(1 for w in words if len(w) >= 2)}")
    if missing and not EXTRA_JSON.exists():
        print("Create example_glosses.json for remaining keys.", file=sys.stderr)
        return 1
    return 0 if not still else 1


if __name__ == "__main__":
    raise SystemExit(main())
