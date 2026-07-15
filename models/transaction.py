from pydantic import BaseModel

class Transaction(BaseModel):
    transactionId: str
    accountId: str
    amount: float
    transactionType: str
    timestamp: str