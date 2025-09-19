from typing import Generator

from sentry_sdk.session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.infrastructure.entity_configuration.base import metadata
import src.infrastructure.entity_configuration.user_model
import src.infrastructure.entity_configuration.address_model

engine = create_engine("postgresql://sa:123456@127.0.0.1:5432/mydb")

SessionLocal = sessionmaker(bind=engine, autoflush=True)

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()