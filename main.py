from fastapi import FastAPI
from controllers.customer_controller import router as customerRouter
from controllers.account_controller import router as accountRouter
from controllers.transaction_controller import router as transactionRouter

# Creates the API
app = FastAPI()

# Includes the controller routers
app.include_router(customerRouter)
app.include_router(accountRouter)
app.include_router(transactionRouter)