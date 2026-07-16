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

    def loginCustomer(self, username, password):
        customer = self.repository.getCustomerByUsername(username)

        if customer is None:
            return {
                "success": False,
                "message": "User not found"
            }

        if customer["password"] != password:
            return {
                "success": False,
                "message": "Incorrect password"
            }

        return {
            "success": True,
            "customerId": customer["customerId"],
            "username": customer["username"]
        }