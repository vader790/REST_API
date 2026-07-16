from repositories.account_repository import AccountRepository
from datetime import datetime
import uuid
from repositories.transaction_repository import TransactionRepository

# Service
class AccountService:

    def __init__(self):
        self.repository = AccountRepository()
        self.transactionRepository = TransactionRepository()

    def getAllAccounts(self):
        return self.repository.getAllAccounts()

    def getOneAccount(self, accountId):
        return self.repository.getOneAccount(accountId)

    def getAccountsByCustomer(self, customerId):
        return self.repository.getAccountsByCustomer(customerId)

    def createAccount(self, account):
        return self.repository.createAccount(account)

    def updateAccount(self, accountId, account):
        return self.repository.updateAccount(accountId, account)

    def deleteAccount(self, accountId):
        return self.repository.deleteAccount(accountId)

    def deposit(self, accountId, amount):

        account = self.repository.getOneAccount(accountId)

        if not account:
            raise Exception("Account not found")

        newBalance = account["balance"] + amount

        self.repository.updateBalance(accountId, newBalance)

        # Create a transaction record for the deposit
        transaction = {
            "transactionId": str(uuid.uuid4()),
            "accountId": accountId,
            "amount": amount,
            "transactionType": "DEPOSIT",
            "timestamp": datetime.now().isoformat()
        }

        self.transactionRepository.createTransaction(transaction)

        return {
            "message": "Deposit successful",
            "balance": newBalance
        }

    def withdraw(self, accountId, amount):

        account = self.repository.getOneAccount(accountId)

        if not account:
            raise Exception("Account not found")

        if amount > account["balance"]:
            raise Exception("Insufficient funds")

        newBalance = account["balance"] - amount

        self.repository.updateBalance(accountId, newBalance)

        # Create a transaction record for the withdrawal
        transaction = {
            "transactionId": str(uuid.uuid4()),
            "accountId": accountId,
            "amount": amount,
            "transactionType": "WITHDRAWAL",
            "timestamp": datetime.now().isoformat()
        }

        self.transactionRepository.createTransaction(transaction)

        return {
            "message": "Withdrawal successful",
            "balance": newBalance
        }
    