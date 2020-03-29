"""
This file is a helper module which will contain
important functions which I may use again in
other problems.
"""


# This decorator will allow the use of memoization.
from functools import lru_cache


golden_ratio = (1 + 5 ** 0.5) / 2


@lru_cache(maxsize=3000)
def fib(term):
    """
    This is a recursive fibonacci function.
    """
    if term == 1:
        return 1
    if term == 2:
        return 2
    elif term > 1:
        return fib(term - 1) + fib(term - 2)


if __name__ == "__main__":
    pass
