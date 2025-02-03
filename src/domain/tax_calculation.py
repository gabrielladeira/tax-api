from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from src.domain.models.tax_rate import TaxType

from src.domain.models.tax_rate import TaxRate


class TaxCalculation(ABC):
    @abstractmethod
    def calculate(
        self, revenue_without_withholding: float, revenue_with_withholding: float, tax_rate: TaxRate
    ) -> float:
        raise NotImplementedError()


class PISTax(TaxCalculation):
    def calculate(
        self, revenue_without_withholding: float, revenue_with_withholding: Optional[float], tax_rate: TaxRate
    ) -> float:
        value = revenue_without_withholding * tax_rate.base_tax_rate

        if not revenue_with_withholding:
            return value

        return value - (revenue_with_withholding * tax_rate.withholding_tax_rate)


class COFINSTax(TaxCalculation):
    def calculate(
        self, revenue_without_withholding: float, revenue_with_withholding: Optional[float], tax_rate: TaxRate
    ) -> float:
        value = revenue_without_withholding * tax_rate.base_tax_rate

        if not revenue_with_withholding:
            return value

        return value - (revenue_with_withholding * tax_rate.withholding_tax_rate)


class CLSSTax(TaxCalculation):
    def calculate(
        self, revenue_without_withholding: float, revenue_with_withholding: Optional[float], tax_rate: TaxRate
    ) -> float:
        if tax_rate.presumide_tax_rate is None:
            raise ValueError("Para cálculo de CLSS, a alíquota de presução é obrigatória")

        value = revenue_without_withholding * tax_rate.base_tax_rate * tax_rate.presumide_tax_rate

        if not revenue_with_withholding:
            return value

        return (
            value
            + (revenue_with_withholding * tax_rate.base_tax_rate * tax_rate.presumide_tax_rate)
            - (revenue_with_withholding * tax_rate.presumide_tax_rate * tax_rate.withholding_tax_rate)
        )


class TaxCalculationStrategy:
    def __init__(self) -> None:
        self._strategies: List[Tuple[TaxType, TaxCalculation]] = [
            (TaxType.PIS, PISTax),
            (TaxType.COFINS, COFINSTax),
            (TaxType.CLSS, CLSSTax),
        ]

    def get_calculation(self, tax_type: TaxType) -> TaxCalculation:
        tax_class = next((tax_class for t, tax_class in self._strategies if t == tax_type), None)

        if tax_class is None:
            raise NotImplementedError()

        tax_class()
