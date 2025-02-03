from abc import abstractmethod
from sqlmodel import Session, select

from src.infraestructure.repositories.base_repository import AbstractRepository, BaseRespository
from src.domain.models.tax_rate import TaxRate, TaxRateType


class TaxRateRepositoryBase(AbstractRepository):
    @abstractmethod
    def find_by_tax_type_and_period(self, tax_type: TaxRateType, tax_period: str) -> TaxRate | None:
        raise NotImplementedError()


class TaxRateRepository(BaseRespository[TaxRate], TaxRateRepositoryBase):
    def __init__(self, session: Session) -> None:
        super().__init__(session, TaxRate)

    def find_by_tax_type_and_period(self, tax_type: TaxRateType, tax_period: str) -> TaxRate | None:
        query = select(TaxRate).where(
            TaxRate.tax_type == tax_type and TaxRate.tax_period == tax_period and TaxRate.active
        )

        return self._session.exec(query).first()
