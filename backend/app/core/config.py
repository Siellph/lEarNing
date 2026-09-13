from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    DATABASE_URL: str = "postgresql://lumina:lumina_dev_password@localhost:5432/lumina"
    SECRET_KEY: str = "change-this-to-a-long-random-string"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440  # 24 hours
    BACKEND_CORS_ORIGINS: str = "http://localhost,http://localhost:80,http://127.0.0.1"
    PUBLIC_APP_URL: str = "http://localhost:3000"
    SMTP_HOST: str = ""
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_FROM: str = "lEarNinG <noreply@example.com>"
    SMTP_USE_TLS: bool = True
    SMTP_USE_SSL: bool = False
    ADMIN_EMAIL: str = ""
    ADMIN_PASSWORD: str = ""
    ADMIN_NAME: str = "Администратор"
    # Fallback when site_settings row is missing; admin UI overrides via DB.
    EMAIL_VERIFICATION_REQUIRED: bool = True

    @property
    def cors_origins(self) -> list[str]:
        return [origin.strip() for origin in self.BACKEND_CORS_ORIGINS.split(",") if origin.strip()]


settings = Settings()
