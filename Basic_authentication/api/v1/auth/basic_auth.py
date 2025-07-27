#!/usr/bin/env python3
"""
Module for BasicAuth class
"""
import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class
    """
    def __init__(self) -> None:
        """
        Initialize BasicAuth
        """
        super().__init__()

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extract the Base64 part of the Authorization header
        for Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        Decode the Base64 part of the Authorization header
        for Basic Authentication
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_header = base64.b64decode(base64_authorization_header)
            return decoded_header.decode('utf-8')
        except Exception:
            return None
