#!/usr/bin/env python3
"""
0. Async Generator
"""


import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """
    Asynchronous generator that yields a random number between 0 and 10.
    It waits for 1 second before yielding each number.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)