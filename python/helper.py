"""
This file is a helper module which will contain
important functions which I may use again in
other problems.
"""


from math import floor, log

# This decorator will allow the use of memoization.
from functools import lru_cache


GOLDEN_RATIO = (1 + 5 ** 0.5) / 2


@lru_cache(maxsize=None)
def collatz(num):
    """
    Will use `num` to perform the Collatz sequence.

    Will then return how many iterations were carried out.
    """
    if num == 1:
        return 1
    elif not num % 2:
        return 1 + collatz(num / 2)
    return 1 + collatz(3 * num + 1)


@lru_cache(maxsize=None)
def fib(n):
    """
    A recursive fibonacci function.

    In this case the fibonacci functions starts as:
    1, 2, 3, 5...
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


def fib_term_from_value(n):
    """
    Finds the term x such that fib(x) == n

    The formula used can be found on:
    https://en.wikipedia.org/wiki/Fibonacci_number#Computation_by_rounding
    """
    return floor(log((n * (5 ** 0.5) + 0.5), GOLDEN_RATIO))


def prime_upper_bound(n):
    """
    Returns the index of the prime number (`n`) in question as well as the
    upper bound when searching for this `n`'th prime number.

    The upper bound was found from
    https://math.stackexchange.com/questions/1270814/bounds-for-n-th-prime
    """
    return {
        "index": n,
        "upper_bound": floor(n * (log(n) + log(log(n))))
    }


def prime_sieve(bound):
    """
    Uses the Sieve of Eratosthenes to generate primes up-to and
    including the upper bound.
    """
    # The if-else below allows the function to either find primes up-till
    # a `n`-th prime, or just find primes below a certain value.
    # This allows usage of `upper_bound()` in conjunction with this function
    if type(bound) == dict:
        n = bound["index"]
        up_bound = bound["upper_bound"]
    else:
        up_bound = bound

    # The actual Sieve of Eratosthenes algorithm

    nums = {i for i in range(3, up_bound, 2)} | {2}
    # Added on the first prime of 2, since it wasn't included
    # when counting the odd numbers
    p = 3

    while p ** 2 < up_bound:
        p_mults = {i for i in range(p ** 2, up_bound, 2 * p)}
        nums = nums.difference(p_mults)
        # Removes all the marked numbers from `nums`
        for x in sorted(list(nums)):
            if x > p:
                p = x
                break
        continue

    if type(bound) == dict:
        return sorted(list(nums))[:n]
        # This will give us the primes up-till but not including the `n`'th prime
        # This is useful if we want the `n`'th prime but only have an
        # approximate upper bound
    return sorted(list(nums))


def get_digits(num):
    """
    Returns all of the digits of `num` as a list of integers
    """
    num = str(num)
    digits = [int(char) for char in num]
    return digits


if __name__ == "__main__":
    pass
