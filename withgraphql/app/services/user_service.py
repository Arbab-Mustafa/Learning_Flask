from app.config.db import db

users_collection = db["users"]

# Get user by username
def get_user_by_username(username):
    user = users_collection.find_one({"username": username})
    if user:
        return {"username": user["username"], "email": user["email"]}
    return None

# Create user
def create_user(username, email):
    if get_user_by_username(username):  # Check if user already exists
        return None
    user_data = {"username": username, "email": email}
    users_collection.insert_one(user_data)
    return user_data

# Delete user
def delete_user(username):
    result = users_collection.delete_one({"username": username})
    return result.deleted_count > 0  # True if user was deleted, False otherwise


# Get all users
def  get_all_users():
    users = list(users_collection.find({}, {"_id": 0, "username": 1, "email": 1}))  
    print("Fetched users:", users)  # 🔍 Debugging line to see if data is retrieved
    return users
