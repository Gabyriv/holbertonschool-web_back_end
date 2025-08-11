#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, jsonify, request
from auth import Auth

AUTH = Auth()


app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome():
    """
    Welcome route
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
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


if __name__ == "__main__":
    """
    Main function
    """
    app.run(host="0.0.0.0", port="5000")
