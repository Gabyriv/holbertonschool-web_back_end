#!/usr/bin/env python3
"""
2. Run time for four parallel comprehensions
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of waiting for the completion
    of 4 parallelized tasks.

    Returns:
        float: Total runtime in seconds.
    """
    starting_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))

    ending_time = time.perf_counter()

    total_time = ending_time - starting_time
    return total_time
