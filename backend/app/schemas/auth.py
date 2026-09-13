from datetime import datetime

from pydantic import BaseModel, Field, field_validator


def _normalize_email(value: str) -> str:
    email = value.strip().lower()
    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError("Некорректный email")
    return email


class RegisterIn(BaseModel):
    email: str = Field(min_length=5, max_length=255)
    name: str = Field(min_length=2, max_length=120)
    password: str = Field(min_length=6, max_length=128)
    accepted_terms: bool = False

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        return _normalize_email(value)


class LoginIn(BaseModel):
    email: str
    password: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        return _normalize_email(value)


class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"


class RegisterOut(BaseModel):
    message: str
    email: str


class MessageOut(BaseModel):
    message: str


class EmailIn(BaseModel):
    email: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        return _normalize_email(value)


class VerifyIn(BaseModel):
    token: str = Field(min_length=8, max_length=256)


class UserOut(BaseModel):
    id: int
    email: str
    name: str
    role: str
    email_verified: bool
    xp: int
    streak: int
    last_activity: datetime | None
    created_at: datetime

    model_config = {"from_attributes": True}


class UserUpdateIn(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=120)
    password: str | None = Field(default=None, min_length=6, max_length=128)
    is_active: bool | None = None
    role: str | None = None
    email_verified: bool | None = None
