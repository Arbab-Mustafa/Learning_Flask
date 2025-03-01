from pymongo import MongoClient
import os

# Load MongoDB URI from .env file or use default
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["flask_graphql"]  # Database name
