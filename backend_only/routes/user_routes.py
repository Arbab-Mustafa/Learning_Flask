from flask import Blueprint, jsonify, request# Ensure you have initialized PyMongo in config
from model.user_model import serialize_user
from datetime import datetime
from config import mongo  # ✅ Import mongo properly
from bson import ObjectId
from werkzeug.security import generate_password_hash
import re

user_bp = Blueprint("user_bp", __name__)


# GET all users
@user_bp.route("/users", methods=["GET"])   
def get_users():
    try:
        # Get all user documents from the database
        users = mongo.db.users.find()
        # Serialize the MongoDB users to JSON
        return jsonify([serialize_user(user) for user in users])
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@user_bp.route("/user", methods=["POST"])
def create_user():
    try:
        data = request.get_json()

        # Validate required fields
        if not data or not all(k in data for k in ["name", "email", "password"]):
            return jsonify({"error": "Name, email, and password are required"}), 400

        name = data["name"].strip()
        email = data["email"].strip().lower()
        password = data["password"]

         

        # Validate password strength
        if len(password) < 6:
            return jsonify({"error": "Password must be at least 6 characters long"}), 400

        # Check if user already exists
        if mongo.db.users.find_one({"email": email}):
            return jsonify({"error": "User with this email already exists"}), 409

        # Hash password
        hashed_password = generate_password_hash(password)

        # Save user to DB
        new_user = {"name": name, "email": email, "password": hashed_password}
        inserted_user = mongo.db.users.insert_one(new_user)

        # Return success response (exclude password)
        new_user["_id"] = str(inserted_user.inserted_id)
        

        return jsonify({"message": "User created successfully", "user": new_user}), 201
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500




@user_bp.route("/user/<id>", methods=["GET"])
def get_user(id):
    try:
        # Convert id to ObjectId
        user = mongo.db.users.find_one({"_id": ObjectId(id)})

        if user:
            return jsonify(serialize_user(user))

        return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@user_bp.route("/user/<id>", methods=["DELETE"])
def delete_user(id):

    try:
        # Convert id to ObjectId
        result = mongo.db.users.delete_one({"_id": ObjectId(id)})

        if result.deleted_count:
            return jsonify(
                {"message": "User deleted successfully", "id": str(id)}
            )

        return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@user_bp.route("/user/<id>", methods=["PUT"])
def update_user(id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided to update"}), 400

        # Convert id to ObjectId
        user = mongo.db.users.find_one({"_id": ObjectId(id)})

        if user:
            mongo.db.users.update_one(
                {"_id": ObjectId(id)},
                {"$set": data},
                
                
            )
            return jsonify({"message": "User updated successfully", "id": str(id)})
        return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

