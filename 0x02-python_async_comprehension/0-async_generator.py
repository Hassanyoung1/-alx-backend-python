#!/usr/bin/python3
""" a coroutine called async_generator that takes no arguments."""
import asyncio
import random


async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
