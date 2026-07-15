from database.mongodb import customer_collection

class CustomerRepository:

    def get_all_customers(self):

        return list(
            customer_collection.find({}, {"_id": 0})
        )
    
    def create_customer(self, customer):
        customer_collection.insert_one(customer)
        return customer