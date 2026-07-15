import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()
uri = os.getenv("MONGO_URI")
db_name = os.getenv("MONGODB_DB")

client = MongoClient(uri)

db = client[db_name]

customerCollection = db["customers"]
accountCollection = db["accounts"]
transactionCollection = db["transactions"]
