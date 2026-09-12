from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_current_user
from app.core.security import create_access_token, hash_password, verify_password
from app.models.user import EmailVerificationToken, User
from app.schemas.auth import (
    EmailIn,
    LoginIn,
    MessageOut,
    RegisterIn,
    RegisterOut,
    TokenOut,
    UserOut,
    UserUpdateIn,
    VerifyIn,
)
from app.services.email import hash_token, issue_verification

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=RegisterOut)
def register(payload: RegisterIn, db: Session = Depends(get_db)):
    if not payload.accepted_terms:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Необходимо принять Пользовательское соглашение и Политику конфиденциальности",
        )
    if db.query(User).filter(User.email == payload.email.lower()).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email уже зарегистрирован")
    user = User(
        email=payload.email.lower(),
        name=payload.name.strip(),
        hashed_password=hash_password(payload.password),
        role="student",
        email_verified=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    issue_verification(db, user)
    return RegisterOut(
        message="Проверьте почту — мы отправили ссылку для подтверждения.",
        email=user.email,
    )


@router.post("/login", response_model=TokenOut)
def login(payload: LoginIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email.lower()).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверный email или пароль")
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Аккаунт отключён")
    if not user.email_verified:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Подтвердите email. Мы отправили ссылку на почту. Если письма нет, запросите его ещё раз.",
        )
    return TokenOut(access_token=create_access_token(str(user.id), {"role": user.role}))


def _confirm_token(raw: str, db: Session) -> MessageOut:
    token_hash = hash_token(raw.strip())
    row = db.query(EmailVerificationToken).filter(EmailVerificationToken.token_hash == token_hash).first()
    if not row:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Ссылка недействительна или уже использована")
    expires = row.expires_at
    if expires.tzinfo is None:
        expires = expires.replace(tzinfo=timezone.utc)
    if expires < datetime.now(timezone.utc):
        db.delete(row)
        db.commit()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Срок ссылки истёк. Запросите письмо ещё раз.")
    user = db.get(User, row.user_id)
    if not user or not user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Аккаунт не найден")
    user.email_verified = True
    db.delete(row)
    db.add(user)
    db.commit()
    return MessageOut(message="Email подтверждён. Теперь можно войти.")


@router.get("/verify", response_model=MessageOut)
def verify_get(token: str = Query(min_length=8, max_length=256), db: Session = Depends(get_db)):
    return _confirm_token(token, db)


@router.post("/verify", response_model=MessageOut)
def verify_post(payload: VerifyIn, db: Session = Depends(get_db)):
    return _confirm_token(payload.token, db)


@router.post("/resend-verification", response_model=MessageOut)
def resend_verification(payload: EmailIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email.lower()).first()
    if user and user.is_active and not user.email_verified:
        issue_verification(db, user)
    return MessageOut(message="Если аккаунт существует и ещё не подтверждён, мы отправили письмо.")


@router.get("/me", response_model=UserOut)
def me(user: User = Depends(get_current_user)):
    return user


@router.patch("/me", response_model=UserOut)
def update_me(payload: UserUpdateIn, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if payload.name:
        user.name = payload.name.strip()
    if payload.password:
        user.hashed_password = hash_password(payload.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
