#!/usr/bin/env python3
"""
Simple REST API built with Flask to manage users.

Features:
- Home route
- Status check
- Retrieve list of users
- Access information for a specific user
- Add a new user via POST request
"""

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """Displays a welcome message at the root of the API."""
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """Returns the list of registered usernames."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Returns 'OK' to verify that the API is running."""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Returns data for a specific user, if they exist."""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a user from JSON data sent via a POST request."""
    data = request.get_json()

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
