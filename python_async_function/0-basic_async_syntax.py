#!/usr/bin/env python3
"""
Asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10)
named wait_random that waits for a random delay between 0 and max_delay
(included and float value)
seconds and eventually returns it.
"""

import random
import asyncio


# Couroutine function
async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay
    (included and float value) seconds and eventually returns it.

    Args:
        max_delay (int, optional): The maximum delay. Defaults to 10.

    Returns:
        int: The actual delay used.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
