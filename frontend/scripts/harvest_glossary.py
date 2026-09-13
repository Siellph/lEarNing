#!/usr/bin/env python3
"""Harvest English words from lesson example sentences and report glossary gaps.

Sources (lesson examples only — not quiz prompts):
  - ex(\"en\", \"ru\") in backend/app/seed/*.py
  - compare left/right strings in theory_*.py / module lessons
  - THEORY overrides that use the same shapes

Writes missing keys (relative to frontend/src/lib/glossary.ts) to stdout.
Optional: --write-stub prints suggested TS entries (English key only; RU must be filled).

Regenerate coverage after expanding seeds:
  python frontend/scripts/harvest_glossary.py
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SEED = REPO / "backend" / "app" / "seed"
GLOSSARY_TS = REPO / "frontend" / "src" / "lib" / "glossary.ts"

WORD_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
EX_DQ = re.compile(r'ex\(\s*"((?:\\.|[^"\\])*)"\s*,', re.S)
EX_SQ = re.compile(r"ex\(\s*'((?:\\.|[^'\\])*)'\s*,", re.S)
COMPARE_PAIR = re.compile(
    r'\{\s*"left"\s*:\s*"((?:\\.|[^"\\])*)"\s*,\s*"right"\s*:\s*"((?:\\.|[^"\\])*)"',
    re.S,
)
GLOSS_ENTRY = re.compile(r'^\s*([a-z][a-z0-9\']*)\s*:\s*"', re.M)


def unescape_dq(raw: str) -> str:
    try:
        return ast.literal_eval('"' + raw + '"')
    except Exception:
        return raw.replace('\\"', '"').replace("\\n", "\n")


def unescape_sq(raw: str) -> str:
    try:
        return ast.literal_eval("'" + raw + "'")
    except Exception:
        return raw.replace("\\'", "'").replace("\\n", "\n")


def normalize_key(word: str) -> str:
    key = word.lower()
    key = re.sub(r"^[^a-z']+|[^a-z']+$", "", key)
    if key.endswith("'s"):
        key = key[:-2]
    if key.endswith("n't"):
        # parallel to lookupGloss: map n't → look up base + "not" separately
        key = key[:-3]
    return key


def collect_sentences() -> list[str]:
    sentences: list[str] = []
    for path in sorted(SEED.glob("*.py")):
        text = path.read_text(encoding="utf-8")
        for m in EX_DQ.finditer(text):
            sentences.append(unescape_dq(m.group(1)))
        for m in EX_SQ.finditer(text):
            sentences.append(unescape_sq(m.group(1)))
        for m in COMPARE_PAIR.finditer(text):
            for g in m.groups():
                s = unescape_dq(g)
                if re.search(r"[A-Za-z]", s):
                    sentences.append(s)
    return sentences


def words_from_sentences(sentences: list[str]) -> set[str]:
    words: set[str] = set()
    for s in sentences:
        for w in WORD_RE.findall(s):
            key = normalize_key(w)
            if key and len(key) >= 1:
                words.add(key)
            # also ensure "not" from n't forms is considered
            if w.lower().endswith("n't"):
                words.add("not")
    return words


def load_glossary_keys() -> set[str]:
    text = GLOSSARY_TS.read_text(encoding="utf-8")
    return set(GLOSS_ENTRY.findall(text))


# Intentional non-words / tokenizer artifacts from linking demos & accent splits
IGNORE = frozenset({"napple", "ca", "wo", "caf", "b", "c", "m", "p"})


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if any harvested word is missing from glossary.ts",
    )
    ap.add_argument(
        "--list-all",
        action="store_true",
        help="Print all harvested words (not only missing)",
    )
    args = ap.parse_args()

    sentences = collect_sentences()
    words = words_from_sentences(sentences)
    known = load_glossary_keys()
    missing = sorted(
        w for w in words if len(w) >= 2 and w not in known and w not in IGNORE
    )
    short = sorted(w for w in words if len(w) < 2 and w not in IGNORE)

    print(f"examples: {len(sentences)}")
    print(f"unique words (len>=2): {sum(1 for w in words if len(w) >= 2)}")
    print(f"glossary keys: {len(known)}")
    print(f"missing: {len(missing)}")
    if short:
        print(f"short (len<2): {', '.join(short)}")
    if args.list_all:
        for w in sorted(words):
            if w in IGNORE:
                mark = "IGN"
            elif w in known or len(w) < 2:
                mark = "OK"
            else:
                mark = "MISS"
            print(f"  {mark}\t{w}")
    else:
        for w in missing:
            print(w)

    if args.check and missing:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
