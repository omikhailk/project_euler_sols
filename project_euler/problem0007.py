"""
What is the 10,001st prime number?
"""


from helper import upper_bound, prime_sieve


def nth_prime(n):
    """
    Will return the last prime number (the `n`-th one) from the list of primes
    generated using the `prime_sieve` function.
    """
    return prime_sieve(upper_bound(n))[-1]


def main():
    print(nth_prime(10001))


if __name__ == '__main__':
    main()
