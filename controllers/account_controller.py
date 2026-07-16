from fastapi import APIRouter
from services.account_service import AccountService
from models.account import Account

router = APIRouter()

service = AccountService()

# Defines the route to get all accounts
@router.get("/api/accounts")
def getAccounts():
    return service.getAllAccounts()

# Defines the route to get a single account
@router.get("/api/accounts/{accountId}")
def getAccount(accountId: str):
    return service.getOneAccount(accountId)

# Defines the route to get all accounts for a specific customer
@router.get("/api/accounts/customer/{customerId}")
def getAccountsByCustomer(customerId: str):
    return service.getAccountsByCustomer(customerId)

# Defines the route to create a new account
@router.post("/api/accounts")
def createAccount(account: Account):
    return service.createAccount(account.model_dump())

# Defines the route to update an existing account
@router.put("/api/accounts/{accountId}")
def updateAccount(accountId: str, account: Account):
    return service.updateAccount(accountId, account.model_dump())

# Defines the route to delete an existing account
@router.delete("/api/accounts/{accountId}")
def deleteAccount(accountId: str):
    return service.deleteAccount(accountId)

# Defines the route to deposit money into an account
@router.post("/api/accounts/{accountId}/deposit")
def deposit(accountId: str, amount: float):
    return service.deposit(accountId, amount)

# Defines the route to withdraw money from an account
@router.post("/api/accounts/{accountId}/withdraw")
def withdraw(accountId: str, amount: float):
    return service.withdraw(accountId, amount)