import pytest

from sqlmodel import Session

from src.domain.models.tax_rate import TaxRate, TaxRateType
from src.infraestructure.repositories.tax_rate_repository import TaxRateRepository


class TestTaxRateRepository:
    @pytest.fixture(autouse=True)
    def setup(self, inmemory_db_session: Session):
        self._session = inmemory_db_session

    def test_should_return_a_tax_rate_when_call_tax_type_and_period(self):
        pis = TaxRate(tax_type=TaxRateType.PIS, tax_period="2025", base_tax_rate=0.65, withholding_tax_rate=0.65)
        cofins = TaxRate(tax_type=TaxRateType.COFINS, base_tax_rate=3.0, tax_period="2025", withholding_tax_rate=3.0)
        clss = TaxRate(
            tax_type=TaxRateType.CLSS,
            base_tax_rate=9.0,
            tax_period="2025",
            presumide_tax_rate=32.0,
            withholding_tax_rate=9.0,
        )
        self._session.add_all([pis, cofins, clss])
        self._session.commit()

        taxRateRepository = TaxRateRepository(self._session)
        result = taxRateRepository.find_by_tax_type_and_period(TaxRateType.PIS, "2025")

        assert result is not None
        assert result.tax_type == TaxRateType.PIS
        assert result.base_tax_rate == 0.65
        assert result.tax_period == "2025"
        assert result.withholding_tax_rate == 0.65
        assert result.presumide_tax_rate is None
        assert result.active is True
        assert result.created_at is not None
        assert result.updated_at is not None

    def test_should_return_none_when_call_tax_type_and_period(self):
        pis = TaxRate(tax_type=TaxRateType.PIS, tax_period="2025", base_tax_rate=0.65, withholding_tax_rate=0.65)
        self._session.add_all([pis])
        self._session.commit()

        taxRateRepository = TaxRateRepository(self._session)
        result = taxRateRepository.find_by_tax_type_and_period(TaxRateType.COFINS, "2025")

        assert result is None
