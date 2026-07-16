from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.customer_controller import router as customerRouter
from controllers.account_controller import router as accountRouter
from controllers.transaction_controller import router as transactionRouter

# Creates the API
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Includes the controller routers
app.include_router(customerRouter)
app.include_router(accountRouter)
app.include_router(transactionRouter)