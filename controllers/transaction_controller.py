from fastapi import APIRouter
from services.transaction_service import TransactionService
from models.transaction import Transaction

router = APIRouter()

service = TransactionService()

# Defines the route to get all transactions
@router.get("/api/transactions")
def getTransactions(accountId: str):
    return service.getAllTransactions(accountId)

# Defines the route to get a single transaction
@router.get("/api/transactions/{transactionId}")
def getTransaction(transactionId: str, accountId: str):
    return service.getOneTransaction(transactionId, accountId)

# Defines the route to create a new transaction
@router.post("/api/transactions")
def createTransaction(transaction: Transaction):
    return service.createTransaction(transaction.model_dump())

# Defines the route to update an existing transaction
@router.put("/api/transactions/{transactionId}")
def updateTransaction(transactionId: str, accountId: str, transaction: Transaction):
    return service.updateTransaction(transactionId, accountId, transaction.model_dump())

# Defines the route to delete an existing transaction
@router.delete("/api/transactions/{transactionId}")
def deleteTransaction(transactionId: str, accountId: str):
    return service.deleteTransaction(transactionId, accountId)