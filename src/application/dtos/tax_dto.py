from sqlmodel import SQLModel, Field
from src.domain.models.tax_rate import TaxType


class CompanyDTO(SQLModel):
    document_numer: str = Field(nullable=False, min_length=14, max_length=14)


class TaxDTO(SQLModel):
    tax_type: TaxType = Field(nullable=False)
    tax_period: str = Field(nullable=False)
    company: CompanyDTO = Field(nullable=False)
    revenue_without_withholding: float = Field(nullable=False, ge=0)
    revenue_with_withholding: float = Field(nullable=False, default=0, ge=0)
