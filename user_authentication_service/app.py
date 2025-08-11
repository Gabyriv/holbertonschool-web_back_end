#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, jsonify, request, abort, Response, redirect
from auth import Auth

AUTH = Auth()


app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome() -> Response:
    """
    Welcome route
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user() -> Response:
    """
    Register a new user
    """
    try:
        email = request.form["email"]
        password = request.form["password"]
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login() -> Response:
    """
    Log in a user: validate credentials and create a session.

    Expects form data: "email" and "password".
    On success: set "session_id" cookie and return JSON payload.
    On failure: respond with HTTP 401 Unauthorized.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password or not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    if session_id is None:
        abort(401)

    resp = jsonify({"email": email, "message": "logged in"})
    resp.set_cookie("session_id", session_id)
    return resp


@app.route("/sessions", methods=["DELETE"])
def logout() -> Response:
    """
    Log out a user by destroying their session and redirecting to '/'.

    Reads the 'session_id' cookie, finds user; if none, aborts with 403.
    On success, destroys the session, clears the cookie, and redirects.
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    resp = redirect("/")
    resp.delete_cookie("session_id")
    return resp


@app.route("/profile", methods=["GET"])
def profile() -> Response:
    """
    Return the profile (email) of the user identified by session cookie.

    Expects 'session_id' cookie. If invalid or user not found, aborts 403.
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    return jsonify({"email": user.email})


if __name__ == "__main__":
    """
    Main function
    """
    app.run(host="0.0.0.0", port="5000")
