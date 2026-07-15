from pydantic import BaseModel

class Account(BaseModel):
    accountId: str
    customerId: str
    accountType: str
    pin: str
    balance: float