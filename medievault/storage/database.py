from collections.abc import Generator

from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

from medievault.config import settings


class Base(DeclarativeBase):
    pass


engine = create_engine(
    settings.database_url,
    echo=False,
    pool_pre_ping=True,
)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            logger.exception("Database session error, rolling back")
            raise
