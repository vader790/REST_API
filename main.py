from fastapi import FastAPI
from controllers.customer_controller import router

# Creates the API
app = FastAPI()

# Includes the customer controller router
app.include_router(router)