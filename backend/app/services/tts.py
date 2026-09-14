"""Cache-first Microsoft Edge neural TTS via edge-tts."""

from __future__ import annotations

import asyncio
import hashlib
import logging
import os
import tempfile
import time
from pathlib import Path

import edge_tts

from app.core.config import settings

logger = logging.getLogger(__name__)

MAX_TTS_CHARS = 4000
# Prune target as a fraction of max so we don't thrash near the limit.
_PRUNE_TARGET_RATIO = 0.9

Accent = str  # "uk" | "us"
RatePreset = str  # "slow" | "normal" | "fast"
Gender = str  # "female" | "male"

VOICES: dict[tuple[str, str], str] = {
    ("us", "female"): "en-US-MichelleNeural",
    ("us", "male"): "en-US-EricNeural",
    ("uk", "female"): "en-GB-SoniaNeural",
    ("uk", "male"): "en-GB-RyanNeural",
}

# Approximate map vs previous Web Speech rates (~0.65 / 0.88 / 1.15).
RATE_PERCENTS: dict[str, str] = {
    "slow": "-30%",
    "normal": "-12%",
    "fast": "+20%",
}

_synth_locks: dict[str, asyncio.Lock] = {}
_locks_guard = asyncio.Lock()
_prune_lock = asyncio.Lock()


def cache_dir() -> Path:
    raw = (settings.TTS_CACHE_DIR or "").strip()
    path = Path(raw) if raw else Path(tempfile.gettempdir()) / "learning_tts_cache"
    path.mkdir(parents=True, exist_ok=True)
    return path


def resolve_voice(accent: str, gender: str) -> str:
    key = (accent, gender)
    voice = VOICES.get(key)
    if not voice:
        raise ValueError(f"Unsupported accent/gender: {accent}/{gender}")
    return voice


def resolve_rate(rate: str) -> str:
    value = RATE_PERCENTS.get(rate)
    if not value:
        raise ValueError(f"Unsupported rate: {rate}")
    return value


def cache_key(text: str, accent: str, rate: str, voice: str) -> str:
    payload = f"{text}|{accent}|{rate}|{voice}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _touch(path: Path) -> None:
    """Update atime/mtime so LRU prefers last access over original write time."""
    try:
        now = time.time()
        os.utime(path, (now, now))
    except OSError:
        pass


def _prune_cache(directory: Path, max_bytes: int) -> None:
    """Delete oldest MP3s (by atime, then mtime) until total size <= 0.9 * max."""
    if max_bytes <= 0:
        return

    entries: list[tuple[float, int, Path]] = []
    total = 0
    for path in directory.glob("*.mp3"):
        if path.name.endswith(".partial.mp3"):
            continue
        try:
            st = path.stat()
        except OSError:
            continue
        if st.st_size <= 0:
            continue
        # Prefer last access; fall back to mtime when atime is unreliable.
        rank = st.st_atime if st.st_atime > 0 else st.st_mtime
        entries.append((rank, st.st_size, path))
        total += st.st_size

    if total <= max_bytes:
        return

    target = int(max_bytes * _PRUNE_TARGET_RATIO)
    entries.sort(key=lambda item: item[0])  # oldest access first
    for _rank, size, path in entries:
        if total <= target:
            break
        try:
            path.unlink()
            total -= size
            logger.info("TTS cache pruned %s (%d bytes)", path.name, size)
        except OSError:
            logger.warning("TTS cache prune failed for %s", path, exc_info=True)


async def _maybe_prune(directory: Path) -> None:
    max_bytes = int(settings.TTS_CACHE_MAX_BYTES)
    if max_bytes <= 0:
        return
    async with _prune_lock:
        await asyncio.to_thread(_prune_cache, directory, max_bytes)


async def _lock_for(key: str) -> asyncio.Lock:
    async with _locks_guard:
        lock = _synth_locks.get(key)
        if lock is None:
            lock = asyncio.Lock()
            _synth_locks[key] = lock
        return lock


async def synthesize_cached(
    text: str,
    *,
    accent: str,
    rate: str,
    gender: str,
) -> Path:
    """Return path to an MP3 file, synthesizing only on cache miss."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("Empty text")
    if len(cleaned) > MAX_TTS_CHARS:
        raise ValueError(f"Text too long (max {MAX_TTS_CHARS} characters)")

    voice = resolve_voice(accent, gender)
    rate_pct = resolve_rate(rate)
    key = cache_key(cleaned, accent, rate, voice)
    directory = cache_dir()
    out = directory / f"{key}.mp3"

    if out.is_file() and out.stat().st_size > 0:
        _touch(out)
        return out

    lock = await _lock_for(key)
    async with lock:
        if out.is_file() and out.stat().st_size > 0:
            _touch(out)
            return out

        tmp = out.with_name(f"{key}.partial.mp3")
        try:
            communicate = edge_tts.Communicate(cleaned, voice, rate=rate_pct)
            await communicate.save(str(tmp))
            if not tmp.is_file() or tmp.stat().st_size == 0:
                raise RuntimeError("TTS produced empty audio")
            tmp.replace(out)
        except Exception:
            if tmp.exists():
                try:
                    tmp.unlink()
                except OSError:
                    pass
            logger.exception("edge-tts synthesis failed")
            raise

        await _maybe_prune(directory)
        return out
