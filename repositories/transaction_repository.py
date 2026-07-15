from database.mongodb import transactionCollection

class TransactionRepository:

    def getAllTransactions(self, accountId):
        return list(
            transactionCollection.find({"accountId": accountId}, {"_id": 0})
        )

    def getOneTransaction(self, transactionId, accountId):
        return list(
            transactionCollection.find({"transactionId": transactionId, "accountId": accountId}, {"_id": 0})
        )
    
    def createTransaction(self, transaction):
        transactionCollection.insert_one(transaction)
        transaction.pop("_id", None)
        return transaction

    def updateTransaction(self, transactionId, accountId, transaction):
        result = transactionCollection.update_one(
            {"transactionId": transactionId, "accountId": accountId},
            {"$set": transaction}
        )
        return result.modified_count
    
    def deleteTransaction(self, transactionId):
        result = transactionCollection.delete_one(
            {"transactionId": transactionId}
        )
        return result.deleted_count