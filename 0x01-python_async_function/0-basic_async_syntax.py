#!/usr/bin/python3
"""Contains a coroutine that delays a certain amount of time and returns it"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that waits for a random duration of time.

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: The duration of the random delay.
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
