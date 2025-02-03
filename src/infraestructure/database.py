from typing import Callable
from sqlmodel import create_engine, Session
from settings import Settings


def create_db_engine(settings: Settings, **kwargs):
    return create_engine(settings.database_connection_str, **kwargs)


def create_session_factory(engine) -> Callable[[], Session]:
    return lambda: Session(bind=engine, autocommit=False, autoflush=False)
