from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime
import pytz


class Lot(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    start_date: datetime
    harvest_date: datetime
    yield_value: float
    created_at: datetime = Field(
        default=datetime.now(tz=pytz.timezone("Europe/Madrid"))
    )
