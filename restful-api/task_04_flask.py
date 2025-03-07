#!/usr/bin/python3
"""A simple Flask API for managing users."""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """Return a welcome message for the API's home page."""
    return "Welcome to the Flask API!"


@app.route("/data", methods=['GET'])
def get_usernames():
    """Return a list of all usernames."""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status", methods=['GET'])
def get_status():
    """Return the API status."""
    return "OK"


@app.route("/users/<usernames>", methods=['GET'])
def get_user(usernames):
    """Return user data for the specified username."""
    user = users.get(usernames)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=['POST'])
def add_user():
    """Add a new user to the users dictionary."""
    new_user = request.json
    if 'username' not in new_user:
        return jsonify({"error": "Username is required"}), 400
    username = new_user['username']
    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run()
