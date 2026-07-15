from fastapi import APIRouter
from services.customer_service import CustomerService
from models.customer import Customer

router = APIRouter()

service = CustomerService()

# Defines the route to get all customers
@router.get("/api/customers")
def get_customers():
    return service.get_all_customers()

@router.post("/api/customers")
def create_customer(customer: Customer):
    return service.create_customer(customer.model_dump())