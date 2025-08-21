# ==============================
#   Function Caching in Python
# ==============================

"""
👉 Definition:
    Function caching (also called memoization) is a technique where 
    results of expensive function calls are stored, so the next time 
    the function is called with the same inputs, the cached result is returned 
    instead of re-computing.

👉 Why use it?
    - Improves performance by avoiding repeated expensive computations
    - Useful in recursive functions, heavy I/O operations, and API calls

👉 In Python:
    - Provided by functools.lru_cache
    - lru_cache = Least Recently Used cache
    - Stores a fixed number of results (maxsize)
    - Automatically clears old cache entries when maxsize is exceeded
"""

import time
from functools import lru_cache


# Caching the results of this function
@lru_cache(maxsize=3)   # stores up to 3 recent results
def some_work(n):
    """
    Simulates a time-consuming task
    by sleeping for 'n' seconds.
    """
    print(f"Doing some work for {n} seconds...")
    time.sleep(n)  # simulate delay
    return n


if __name__ == '__main__':
    print("Now running some work...")

    # First call → takes 3 seconds (not cached yet)
    print(some_work(3))

    print("Done.... Calling again")

    # Second call with same argument → returns instantly (cached result)
    print(some_work(3))

    print("Called with a new value")
    # New argument → takes 2 seconds (not cached yet)
    print(some_work(2))

    # Call again with 3 → still cached
    print(some_work(3))
