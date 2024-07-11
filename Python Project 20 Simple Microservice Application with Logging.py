from flask import Flask, jsonify, request
import logging
import requests

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='user_service.log', level=logging.INFO)

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.route('/users', methods=['GET'])
def get_users():
    logging.info("Fetching all users")
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    logging.info(f"Fetching user with id {user_id}")
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    users.append(new_user)
    logging.info(f"Added new user {new_user}")
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(port=5000, debug=True)


