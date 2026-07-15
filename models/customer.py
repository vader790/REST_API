from pydantic import BaseModel

class Customer(BaseModel):
    customerId: str
    firstName: str
    lastName: str
    email: str
    phone: str
    streetAddress: str
    city: str
    state: str
    zipCode: str
    username: str
    password: str