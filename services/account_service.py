from repositories.account_repository import AccountRepository

# Service
class AccountService:

    def __init__(self):
        self.repository = AccountRepository()

    def getAllAccounts(self):
        return self.repository.getAllAccounts()

    def getOneAccount(self, account_id):
        return self.repository.getOneAccount(account_id)

    def createAccount(self, account):
        return self.repository.createAccount(account)

    def updateAccount(self, account_id, account):
        return self.repository.updateAccount(account_id, account)

    def deleteAccount(self, account_id):
        return self.repository.deleteAccount(account_id)