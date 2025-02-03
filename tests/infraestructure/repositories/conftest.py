import pytest

from sqlmodel import SQLModel, Session, create_engine
from typing import Generator


@pytest.fixture
def inmemory_db_session() -> Generator[Session]:
    engine = create_engine("sqlite:///:memory:", echo=True)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

    SQLModel.metadata.drop_all(engine)
