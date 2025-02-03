from src.application.dtos.tax_dto import TaxDTO
from src.domain.exceptions.tax_exceptions import TaxRateNotConfiguredError
from src.infraestructure.unit_of_work import UnitOfWork
from src.infraestructure.database import create_session_factory


class CreateTaxUseCase:
    def execute(self, tax_dto: TaxDTO) -> float:
        with UnitOfWork(session_factory=create_session_factory) as wow:
            tax_rate = wow.tax_rate.find_by_tax_type_and_period(
                tax_type=tax_dto.tax_type, tax_period=tax_dto.tax_period
            )

            if tax_rate is None:
                raise TaxRateNotConfiguredError()

            taxCalculation = self._get_calculation(tax_rate.ty)

            return taxCalculation.calculate(
                revenue_with_withholding=1, revenue_without_withholding=1, tax_rate=tax_rate
            )
