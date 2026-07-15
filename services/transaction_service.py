from repositories.transaction_repository import TransactionRepository

# Service
class TransactionService:

    def __init__(self):
        self.repository = TransactionRepository()

    def getAllTransactions(self, accountId):
        return self.repository.getAllTransactions(accountId)

    def getOneTransaction(self, transactionId, accountId):
        return self.repository.getOneTransaction(transactionId, accountId)

    def createTransaction(self, transaction):
        return self.repository.createTransaction(transaction)

    def updateTransaction(self, transactionId, accountId, transaction):
        return self.repository.updateTransaction(transactionId, accountId, transaction)

    def deleteTransaction(self, transactionId, accountId):
        return self.repository.deleteTransaction(transactionId, accountId)