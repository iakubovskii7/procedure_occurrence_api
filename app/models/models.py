import datetime
from pydantic import BaseModel, Field, PositiveInt

# Pydantic Models
class UniquePersonsResponse(BaseModel):
    n_days: PositiveInt = Field(gt=1, description="Number of last days queried")
    unique_person_count: PositiveInt = Field(ge=0, description="Count of unique persons in the last n days")

class ProvidersAndPersonsResponse(BaseModel):
    procedure_type: int = Field(ge=0, description="Procedure type ID")
    data: dict[datetime.date, dict[str, int]] = Field(
        ..., description="Nested dictionary: {date: {'cnt_providers': X, 'cnt_persons': Y}}"
    )