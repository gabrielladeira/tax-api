from datetime import datetime
from enum import Enum
from sqlmodel import Field, Index, CheckConstraint

from src.domain.models.base_model import BaseModel
from src.domain.shared_resources.datetimes import DateTimes


class TaxType(str, Enum):
    PIS = "PIS"
    COFINS = "COFINS"
    CLSS = "CSLL"


class Tax(BaseModel, table=True):
    __tablename__ = "taxes"

    tax_type: TaxType = Field(nullable=False)
    period: str = Field(nullable=False)
    value: float = Field(ge=0, nullable=False)
    cnpj: str = Field(nullable=False)
    active: bool = Field(default=True, nullable=False)
    created_at: datetime = Field(default_factory=DateTimes.now, nullable=False)
    updated_at: datetime = Field(default_factory=DateTimes.now, nullable=False)

    __table_args__ = (
        CheckConstraint("value >= 0", name="tax_value_gte_zero"),
        Index(
            "idx_tax_active_per_type_period_and_cpnj",
            "tax_type",
            "period",
            "cnpj",
            unique=True,
            postgresql_where="active = TRUE",
        ),
    )
