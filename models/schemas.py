from pydantic import BaseModel
from typing import Optional


class FinancialDocSchema(BaseModel):
    doc_type: str
    amount: float
    currency: str
    doc_date: str
    account_number: Optional[str] = None
