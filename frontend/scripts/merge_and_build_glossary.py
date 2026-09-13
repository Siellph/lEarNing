#!/usr/bin/env python3
"""Rebuild glossary.ts from example_glosses.json (+ existing entries).

  python frontend/scripts/merge_and_build_glossary.py
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from build_glossary import main as build  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(build())
