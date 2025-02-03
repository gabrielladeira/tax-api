from abc import ABC, abstractmethod
from sqlmodel import Session
from typing import Generic, Type, TypeVar

from src.domain.models.base_model import BaseModel

T = TypeVar("T", bound=BaseModel)


class AbstractRepository(Generic[T], ABC):
    @abstractmethod
    def add(self, record: T) -> T:
        raise NotImplementedError()

    @abstractmethod
    def update(self, record: T) -> T:
        raise NotImplementedError()


class BaseRespository(AbstractRepository[T], ABC):
    def __init__(self, session: Session, model_cls: Type[T]) -> None:
        self._session = session
        self._model_cls = model_cls

    def add(self, record: T) -> T:
        self._session.add(record)
        self._session.flush()
        self._session.refresh(record)
        return record

    def update(self, record: T) -> T:
        self._session.add(record)
        self._session.flush()
        self._session.refresh(record)
        return record
