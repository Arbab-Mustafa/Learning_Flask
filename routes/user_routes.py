from flask import Blueprint, request, jsonify
from model.user_model import UserModel

user_bp = Blueprint("user_routes", __name__)

@user_bp.route("/users", methods=["GET"])
def get_users():
    # users = UserModel.get_all_users()
    return 'Hello, World!'
    

 
