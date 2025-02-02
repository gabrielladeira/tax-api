from datetime import datetime
from enum import Enum
from sqlmodel import SQLModel, Field, Index, CheckConstraint
from typing import Optional
from uuid import UUID, uuid4

from src.domain.shared_resources.datetimes import DateTimes


class TaxRateType(str, Enum):
    PIS = "PIS"
    COFINS = "COFINS"
    CLSS = "CSLL"


class TaxRate(SQLModel, table=True):
    __tablename__ = "tax_rates"

    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
    tax_type: TaxRateType = Field(nullable=False)
    tax_period: str = Field(nullable=False)
    base_tax_rate: float = Field(gt=0, nullable=False)
    presumide_tax_rate: Optional[float] = Field(gt=0, nullable=True)
    withholding_tax_rate: float = Field(gt=0, nullable=False)
    active: bool = Field(nullable=False)
    created_at: datetime = Field(default_factory=DateTimes.now, nullable=False)
    updated_at: datetime = Field(default_factory=DateTimes.now, nullable=False)

    __table_args__ = (
        CheckConstraint("base_tax_rate >= 0", name="base_tax_rate_gte_zero"),
        CheckConstraint("presumide_tax_rate >= 0", name="presumide_tax_rate_gte_zero"),
        CheckConstraint(
            "withholding_tax_rate is null or withholding_tax_rate >= 0", name="withholding_tax_rate_gte_zero"
        ),
        Index(
            "idx_tax_type_active_per_type_period",
            "tax_type",
            "tax_period",
            unique=True,
            postgresql_where="active = TRUE",
        ),
    )
