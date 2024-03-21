#!/usr/bin/python3
""" Run time for four parallel comprehensions """
import asyncio
import random
import time 
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start = time.perf_counter()  
    await asyncio.gather(*(async_comprehension() for x in range(4)))
    end = time.perf_counter()
    elapsed = start - end
    return elapsed
   
    
