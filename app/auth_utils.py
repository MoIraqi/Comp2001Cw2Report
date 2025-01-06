from functools import wraps
from flask import request, jsonify


def check_token():
    """Function to check the validity of the token"""
    token = request.headers.get('Authorization')
    if not token:
        return None, "Token is missing"
    # Token validation logic
    if token != "YOUR_VALID_TOKEN":  # Replace this with actual token validation logic
        return None, "Invalid token"
    return token, None


def authenticate_user(func):
    """Decorator to authenticate user based on provided token"""

    @wraps(func)
    def decorated_function(*args, **kwargs):
        token, error = check_token()
        if error:
            return jsonify({"error": error}), 403
        return func(*args, **kwargs)

    return decorated_function


def validate_token(func):
    """Decorator to validate token for accessing routes"""

    @wraps(func)
    def decorated_function(*args, **kwargs):
        token, error = check_token()
        if error:
            return jsonify({"error": error}), 403
        return func(*args, **kwargs)

    return decorated_function
