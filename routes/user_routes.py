from flask import Blueprint, jsonify, request# Ensure you have initialized PyMongo in config
from model.user_model import serialize_user
from datetime import datetime
from config import mongo  # ✅ Import mongo properly
from bson import ObjectId

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

        if not data or "name" not in data or "email" not in data or "password" not in data:
            return jsonify({"error": "Missing required fields"}), 400

        user = {
            "name": data["name"],
            "email": data["email"],
            "password": data["password"],  # ❗ Hash this in production
            "created_at": datetime.now(),

        }

        inserted_id = mongo.db.users.insert_one(user).inserted_id  # ✅ Correct usage
        return jsonify({"message": "User created successfully", "id": str(inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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

