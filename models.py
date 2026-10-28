from typing import Optional
from pydantic import BaseModel


class AnalyzeResponse(BaseModel):
    status: str
    row_count: Optional[int] = None
    column_count: Optional[int] = None
    message: Optional[str] = None
