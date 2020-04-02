"""
This file is a helper module which will contain
important functions which I may use again in
other problems.
"""


from math import floor, log
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


def upper_bound(nth):
    """
    Returns the term and the upper bound for the `nth`
    prime number. This information is returned as a dictionary.

    The upper bound was found from shorturl.at/aqBHQ
    """
    return {
        "index": nth,
        "upper_bound": floor(nth * (log(nth) + log(log(nth))))
    }


def prime_sieve(bound):
    """
    Uses the Sieve of Eratosthenes to generate primes up-to and
    including the upper bound.
    """
    # The if-else below allows the function to either find primes up-till
    # a N-th prime, or just find primes below a certain value.
    # This allows usage of `upper_bound()` in conjunction with this function
    if type(bound) == dict:
        nth = bound["index"]
        up_bound = bound["upper_bound"]
    else:
        up_bound = bound

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
        return sorted(list(nums))[:nth]
        # This will give us the primes up-till the `nth` prime
        # This is useful if we want the `nth` prime and only have an
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
