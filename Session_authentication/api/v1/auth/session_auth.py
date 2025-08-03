#!/usr/bin/env python3
""" Session Auth class module"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Session Auth class """
    def __init__(self) -> None:
        super().__init__()
