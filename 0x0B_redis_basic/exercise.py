#!/usr/bin/env python3
"""
Redis Basic
"""

import redis
from typing import Optional, Union, Callable
import uuid


class Cache:
    """
    Cache class
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get_str(self, key: str) -> Optional[str]:
        """
        Get string data from Redis
        """
        return self.get(key, fn=lambda raw_bytes: raw_bytes.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Get int data from Redis
        """
        return self.get(key, fn=int)

    def get(
        self,
        key: str,
        fn: Callable = None
    ) -> Optional[Union[str, bytes, int, float]]:
        """
        Get data from Redis
        """
        value = self._redis.get(key)
        if value is None:
            return None
        elif fn is not None:
            return fn(value)
        return value
