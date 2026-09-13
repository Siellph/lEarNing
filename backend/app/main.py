from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import admin, assessments, auth, grammar, phonetics, practice, progress, public, study, vocab
from app.core.config import settings
from app import models  # noqa: F401
from app.core.database import Base, engine
from app.seed.expand import ensure_email_verified_column, ensure_site_setting_columns

Base.metadata.create_all(bind=engine)
ensure_email_verified_column(engine)
ensure_site_setting_columns(engine)

app = FastAPI(
    title="lEarNing",
    description="lEarNing — учим EN. Платформа изучения английской грамматики и словарного запаса",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins + ["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api")
app.include_router(grammar.router, prefix="/api")
app.include_router(practice.router, prefix="/api")
app.include_router(assessments.router, prefix="/api")
app.include_router(vocab.router, prefix="/api")
app.include_router(study.router, prefix="/api")
app.include_router(phonetics.router, prefix="/api")
app.include_router(progress.router, prefix="/api")
app.include_router(admin.router, prefix="/api")
app.include_router(public.router, prefix="/api")


@app.get("/api/health")
def health():
    return {"status": "ok"}
