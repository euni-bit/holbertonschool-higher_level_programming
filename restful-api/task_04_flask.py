from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Root endpoint
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Endpoint to return JSON data
@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))

# Endpoint to return status
@app.route('/status')
def get_status():
    return "OK"

# Dynamic endpoint to get user information
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Endpoint to handle POST request and add new user
@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        user_data = request.get_json()
        username = user_data.get('username')

        if not username:
            return jsonify({"error": "Username is required"}), 404
        
        if username in users:
            return jsonify({"error": "User already exists"}), 400
        
        users[username] = {
        "username": username,
        "name": user_data.get('name'),
        "age": user_data.get('age'),
        "city": user_data.get('city')
          }
        return jsonify({"message": "User added","user": users[username]}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run()
