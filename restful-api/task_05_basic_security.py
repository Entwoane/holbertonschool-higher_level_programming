from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_jwt_extended import jwt_required, JWTManager
from flask import Flask, request, jsonify

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "secret-key-super-secret"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def check_password(username, password):
    """
    Verify the password for a given username.

    Args:
        username (str): The username to check.
        password (str): The password to verify.

    Returns:
        str: The username if authentication is successful, None otherwise.
    """
    if (username in users and
            check_password_hash(users[username]['password'], password)):
        return username


@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def basic_protect():
    """
    Protected route that requires basic authentication.

    Returns:
        str: A message indicating successful authentication.
    """
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    Login route to authenticate users and provide JWT tokens.

    Returns:
        tuple: A JSON response with the access token or an error message,
               and the appropriate HTTP status code.
    """
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"error": "401 Unauthorized"}), 401
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Invalid username or password"}), 401


@app.route("/jwt-protected", methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    Protected route that requires a valid JWT token.

    Returns:
        str: A message indicating successful JWT authentication.
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=['GET'])
@jwt_required()
def admin_auth():
    """
    Admin-only route that requires a valid JWT token with admin role.

    Returns:
        tuple: A JSON response with a success message or an error message,
               and the appropriate HTTP status code.
    """
    current_user = get_jwt_identity()
    if users[current_user]['role'] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle unauthorized token errors.

    Args:
        err: The error message from JWT.

    Returns:
        tuple: A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid token errors.

    Args:
        err: The error message from JWT.

    Returns:
        tuple: A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(header, payload):
    """
    Handle expired token errors.

    Args:
        err: The error message from JWT.

    Returns:
        tuple: A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Token has expired"}), 401


if __name__ == "__main__":
    app.run(port=5000)
