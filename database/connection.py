import os

# Prevent Windows Application Control policy DLL blocking by defaulting to pure-Python psycopg driver
os.environ.setdefault("PSYCOPG_IMPL", "python")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg://postgres:1234@localhost:5432/mediassist"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()