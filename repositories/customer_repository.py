from database.mongodb import customerCollection

class CustomerRepository:

    def getAllCustomers(self):
        return list(
            customerCollection.find({}, {"_id": 0})
        )

    def getOneCustomer(self, customerId):
        return customerCollection.find_one({"customerId": customerId}, {"_id": 0})
    
    def createCustomer(self, customer):
        customerCollection.insert_one(customer)
        customer.pop("_id", None)
        return customer

    def updateCustomer(self, customerId, customer):
        result = customerCollection.update_one(
            {"customerId": customerId},
            {"$set": customer}
        )
        return result.modified_count
    
    def deleteCustomer(self, customerId):
        result = customerCollection.delete_one(
            {"customerId": customerId}
        )
        return result.deleted_count