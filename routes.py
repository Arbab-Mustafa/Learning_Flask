from __init__ import app, mongo
from flask import jsonify, request

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    mongo.db.users.insert_one(data)
    return jsonify({"message": "User added successfully"}), 201

@app.route('/get_users', methods=['GET'])
def get_users():
    users = list(mongo.db.users.find({}, {"_id": 0}))
    return jsonify(users)
