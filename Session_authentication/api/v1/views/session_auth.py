#!/usr/bin/env python3
""" Module of Session Authentication views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - User object JSON represented
      - 400 if email or password is missing
      - 404 if no user found for this email
      - 401 if password is wrong
    """
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if email is missing or empty
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400

    # Check if password is missing or empty
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    # Search for user by email
    users = User.search({"email": email})
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    # Validate password
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Import auth only when needed to avoid circular imports
    from api.v1.app import auth

    # Create session ID for the user
    session_id = auth.create_session(user.id)

    # Create response with user JSON
    response = make_response(jsonify(user.to_json()))

    # Set session cookie using SESSION_NAME environment variable
    cookie_name = os.getenv('SESSION_NAME')
    response.set_cookie(cookie_name, session_id)

    return response


@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """ DELETE /api/v1/auth_session/logout
    Return:
      - Empty JSON dictionary with status 200 if successful
      - 404 if session destruction fails
    """
    from api.v1.app import auth

    if not auth.destroy_session(request):
        abort(404)

    return jsonify({})
