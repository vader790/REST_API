from repositories.customer_repository import CustomerRepository

# Service
class CustomerService:

    def __init__(self):
        self.repository = CustomerRepository()

    def get_all_customers(self):
        return self.repository.get_all_customers()

    def create_customer(self, customer):
        return self.repository.create_customer(customer)