from abc import ABC, abstractmethod
from sqlmodel import Session
from typing import Callable

from src.infraestructure.repositories.tax_rate_repository import TaxRateRepository, TaxRateRepositoryBase


class UnitOfWorkBase(ABC):
    tax_rate: TaxRateRepositoryBase

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError()

    @abstractmethod
    def rollback(self):
        raise NotImplementedError()


class UnitOfWork(UnitOfWorkBase):
    def __init__(self, session_factory: Callable[[], Session]) -> None:
        self._session_factory = session_factory

    def __enter__(self):
        self._session = self._session_factory()
        self.tax_rate = TaxRateRepository(self._session)

        return super().__enter__()

    def commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()
