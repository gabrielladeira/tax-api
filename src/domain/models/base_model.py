from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4


class BaseModel(SQLModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
