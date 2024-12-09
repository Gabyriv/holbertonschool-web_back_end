#!/usr/bin/env python3
"""
1. Async Comprehension
"""


import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Async comprehension that collects 10 random numbers between 0 and 10
    and then return them.
    """
    return [i async for i in async_generator()]
