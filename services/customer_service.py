from repositories.customer_repository import CustomerRepository

# Service
class CustomerService:

    def __init__(self):
        self.repository = CustomerRepository()

    def getAllCustomers(self):
        return self.repository.getAllCustomers()

    def getOneCustomer(self, customerId):
        return self.repository.getOneCustomer(customerId)

    def createCustomer(self, customer):
        return self.repository.createCustomer(customer)

    def updateCustomer(self, customerId, customer):
        return self.repository.updateCustomer(customerId, customer)

    def deleteCustomer(self, customerId):
        return self.repository.deleteCustomer(customerId)