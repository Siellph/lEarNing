import hashlib
import logging
import secrets
import smtplib
import socket
import ssl
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
    subject = "Подтвердите email — lEarNinG"
    body = (
        "Здравствуйте!\n\n"
        "Подтвердите адрес электронной почты, чтобы войти в lEarNinG:\n"
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
    attempts = [(port, use_ssl)]
    for fallback_port, fallback_ssl in ((587, False), (465, True), (2525, False)):
        if (fallback_port, fallback_ssl) not in attempts:
            attempts.append((fallback_port, fallback_ssl))
    try:
        smtp = _open_smtp(host, attempts)
        try:
            if settings.SMTP_USER:
                smtp.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            smtp.send_message(msg)
        finally:
            smtp.quit()
    except Exception:
        logger.exception("Не удалось отправить письмо на %s", to_email)
        print(f"VERIFICATION LINK for {to_email}: {link}", flush=True)


def _ipv4_socket(host: str, port: int, timeout: float) -> socket.socket:
    last: OSError | None = None
    for family, socktype, proto, _, sockaddr in socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM):
        sock = socket.socket(family, socktype, proto)
        sock.settimeout(timeout)
        try:
            sock.connect(sockaddr)
            return sock
        except OSError as exc:
            last = exc
            sock.close()
    raise last or OSError(f"Нет IPv4 для {host}:{port}")


def _open_smtp(host: str, attempts: list[tuple[int, bool]], timeout: float = 20) -> smtplib.SMTP:
    errors: list[str] = []
    for port, use_ssl in attempts:
        try:
            raw = _ipv4_socket(host, port, timeout)
            if use_ssl:
                ctx = ssl.create_default_context()
                raw = ctx.wrap_socket(raw, server_hostname=host)
                smtp = smtplib.SMTP_SSL()
            else:
                smtp = smtplib.SMTP()
            smtp.timeout = timeout
            smtp.sock = raw
            code, _ = smtp.getreply()
            if code != 220:
                smtp.close()
                raise smtplib.SMTPConnectError(code, f"{host}:{port}")
            smtp.ehlo_or_helo_if_needed()
            if not use_ssl:
                smtp.starttls()
                smtp.ehlo()
            logger.info("SMTP подключен %s:%s ssl=%s", host, port, use_ssl)
            return smtp
        except OSError as exc:
            errors.append(f"{host}:{port} ssl={use_ssl} -> {exc}")
            logger.warning("SMTP порт недоступен: %s", errors[-1])
    raise ConnectionRefusedError(
        "Исходящий SMTP закрыт (465/587/2525). Хостер часто режет эти порты. "
        + " | ".join(errors)
    )


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
