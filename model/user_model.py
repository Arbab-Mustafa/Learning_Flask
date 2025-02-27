from flask_pymongo import PyMongo

mongo = PyMongo()  # Initialize MongoDB

def serialize_user(user):
    return {
        "_id": str(user["_id"]),  # Convert ObjectId to string
        "name": user.get("name", ""),
        "email": user.get("email", ""),
        "password": user.get("password", ""),  # Consider hashing passwords before storing
        "created_at": user.get("created_at", ""),
    }


