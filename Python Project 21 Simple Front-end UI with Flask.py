from flask import Flask, render_template, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/users', methods=['GET'])
def get_users():
    logging.info("Fetching all users")
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def add_user():
    new_user = request.json
    users.append(new_user)
    logging.info(f"Added new user {new_user}")
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(port=5000, debug=True)
