#!/usr/bin/env python3
"""Generates 10 random numbers asynchronously using list comprehension."""

import asyncio
import random
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """
    async_comprehension- function to return 10 random numbers
    Arguments:
        no arguments
    Returns:
        10 random numbers
    """
    result = [i async for i in async_generator()]
    return result
