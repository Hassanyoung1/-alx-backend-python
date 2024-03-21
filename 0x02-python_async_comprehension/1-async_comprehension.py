#!/usr/bin/env python3
"""Generates 10 random numbers asynchronously using list comprehension."""

import asyncio
import random
from typing import Generator


async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> list[int]:
    """Generates 10 random numbers asynchronously using list comprehension."""
    result = [i async for i in async_generator()]
    return result
