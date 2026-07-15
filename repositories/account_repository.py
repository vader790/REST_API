from database.mongodb import accountCollection

class AccountRepository:

    def getAllAccounts(self):
        return list(
            accountCollection.find({}, {"_id": 0})
        )

    def getOneAccounts(self, accountId):
        return list(
            accountCollection.find({"accountId": accountId}, {"_id": 0})
        )
    
    def createAccount(self, account):
        accountCollection.insert_one(account)
        account.pop("_id", None)
        return account

    def updateAccount(self, accountId, account):
        result = accountCollection.update_one(
            {"accountId": accountId},
            {"$set": account}
        )
        return result.modified_count
    
    def deleteAccount(self, accountId):
        result = accountCollection.delete_one(
            {"accountId": accountId}
        )
        return result.deleted_count