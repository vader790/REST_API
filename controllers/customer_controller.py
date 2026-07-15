from fastapi import APIRouter
from services.customer_service import CustomerService
from models.customer import Customer

router = APIRouter()

service = CustomerService()

# Defines the route to get all customers
@router.get("/api/customers")
def getCustomers():
    return service.getAllCustomers()

# Defines the route to get a single customer
@router.get("/api/customers/{customerId}")
def getCustomer(customerId: str):
    return service.getOneCustomer(customerId)

# Defines the route to create a new customer
@router.post("/api/customers")
def createCustomer(customer: Customer):
    return service.createCustomer(customer.model_dump())

# Defines the route to update an existing customer
@router.put("/api/customers/{customerId}")
def updateCustomer(customerId: str, customer: Customer):
    return service.updateCustomer(customerId, customer.model_dump())

# Defines the route to delete an existing customer
@router.delete("/api/customers/{customerId}")
def deleteCustomer(customerId: str):
    return service.deleteCustomer(customerId)