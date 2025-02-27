from flask_pymongo import PyMongo

mongo = PyMongo()  # Initialize MongoDB

class UserModel:
    @staticmethod
    def create_user(data):
        """Insert a new user into MongoDB"""
        return mongo.db.users.insert_one(data)

    @staticmethod
    def get_user_by_email(email):
        """Find a user by email"""
        return mongo.db.users.find_one({"email": email})

    @staticmethod
    def get_all_users():
        """Get all users"""
        return list(mongo.db.users.find({}, {"password": 0}))  # Exclude password
