import os
from dotenv import load_dotenv
from flask_pymongo import PyMongo

# Load environment variables from .env file
load_dotenv()

class MONGO_Config:
    MONGO_URI = os.getenv("MONGO_URI")  # ✅ Ensure .env has MONGO_URI

mongo = PyMongo()  # ✅ Define `mongo` here to avoid circular imports
