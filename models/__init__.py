from pydantic import BaseModel
from typing import Optional


class FinancialDocSchema(BaseModel):
    doc_type: str  # 문서 종류
    amount: float  # 금액
    currency: str  # 통화 (KRW 등)
    doc_date: str  # 날짜
    account_number: Optional[str] = None  # 계좌번호 (없을 수도 있음)
