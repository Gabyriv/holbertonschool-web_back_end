#!/usr/bin/env python3
"""
Module for BasicAuth class
"""
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
