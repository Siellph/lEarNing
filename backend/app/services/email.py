import hashlib
import logging
import secrets
import smtplib
from datetime import datetime, timedelta, timezone
from email.message import EmailMessage

from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.user import EmailVerificationToken, User

logger = logging.getLogger(__name__)

TOKEN_TTL_HOURS = 24


def generate_raw_token() -> str:
    return secrets.token_urlsafe(32)


def hash_token(raw: str) -> str:
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def verification_link(raw_token: str) -> str:
    return f"{settings.PUBLIC_APP_URL.rstrip('/')}/verify?token={raw_token}"


def send_verification_email(to_email: str, raw_token: str) -> None:
    link = verification_link(raw_token)
    subject = "Подтвердите email — lEarNing"
    body = (
        "Здравствуйте!\n\n"
        "Подтвердите адрес электронной почты, чтобы войти в lEarNing:\n"
        f"{link}\n\n"
        "Ссылка действует 24 часа.\n\n"
        "Если вы не регистрировались, просто проигнорируйте это письмо.\n"
    )

    if not settings.SMTP_HOST:
        print(f"VERIFICATION LINK for {to_email}: {link}", flush=True)
        logger.warning("SMTP не настроен. Ссылка подтверждения для %s: %s", to_email, link)
        return

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = settings.SMTP_FROM
    msg["To"] = to_email
    msg.set_content(body)
    host = settings.SMTP_HOST.strip()
    port = settings.SMTP_PORT
    use_ssl = settings.SMTP_USE_SSL or port == 465
    try:
        factory = smtplib.SMTP_SSL if use_ssl else smtplib.SMTP
        with factory(host, port, timeout=20) as smtp:
            if not use_ssl and settings.SMTP_USE_TLS:
                smtp.starttls()
            if settings.SMTP_USER:
                smtp.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            smtp.send_message(msg)
    except Exception:
        logger.exception("Не удалось отправить письмо на %s", to_email)
        print(f"VERIFICATION LINK for {to_email}: {link}", flush=True)


def issue_verification(db: Session, user: User) -> None:
    raw = generate_raw_token()
    db.query(EmailVerificationToken).filter(EmailVerificationToken.user_id == user.id).delete()
    db.add(
        EmailVerificationToken(
            user_id=user.id,
            token_hash=hash_token(raw),
            expires_at=datetime.now(timezone.utc) + timedelta(hours=TOKEN_TTL_HOURS),
        )
    )
    db.commit()
    send_verification_email(user.email, raw)
