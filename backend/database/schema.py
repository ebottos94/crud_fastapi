from pydantic import BaseModel
from datetime import datetime


class LotCreateSchema(BaseModel):
    start_date: datetime
    harvest_date: datetime
    yield_value: float


class LotUpdateSchema(BaseModel):
    start_date: datetime | None = None
    harvest_date: datetime | None = None
    yield_value: float | None = None
