from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from app.core.deps import get_current_user
from app.models.user import User
from app.services.tts import MAX_TTS_CHARS, synthesize_cached

router = APIRouter(prefix="/tts", tags=["tts"])

AccentParam = Literal["uk", "us"]
RateParam = Literal["slow", "normal", "fast"]
GenderParam = Literal["female", "male"]


class TtsIn(BaseModel):
    text: str = Field(..., min_length=1, max_length=MAX_TTS_CHARS)
    accent: AccentParam = "uk"
    rate: RateParam = "normal"
    gender: GenderParam = "female"


async def _audio_response(
    text: str,
    accent: AccentParam,
    rate: RateParam,
    gender: GenderParam,
) -> FileResponse:
    try:
        path = await synthesize_cached(text, accent=accent, rate=rate, gender=gender)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=502, detail="Не удалось синтезировать речь") from exc

    return FileResponse(
        path,
        media_type="audio/mpeg",
        filename="speech.mp3",
        headers={"Cache-Control": "private, max-age=86400"},
    )


@router.get("")
async def tts_get(
    text: str = Query(..., min_length=1, max_length=MAX_TTS_CHARS),
    accent: AccentParam = Query("uk"),
    rate: RateParam = Query("normal"),
    gender: GenderParam = Query("female"),
    _: User = Depends(get_current_user),
):
    return await _audio_response(text, accent, rate, gender)


@router.post("")
async def tts_post(payload: TtsIn, _: User = Depends(get_current_user)):
    return await _audio_response(payload.text, payload.accent, payload.rate, payload.gender)
