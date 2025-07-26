#!/usr/bin/env python3
"""
Module that encrypts passwords
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt

    Args:
        password: The password to hash

    Returns:
        A salted, hashed password, which is a byte string
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
