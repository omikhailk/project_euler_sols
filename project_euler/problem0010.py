"""
Find the sum of all the primes below two million.
"""


from helper import prime_sieve


def sum_of_primes(limit):
    """
    Uses the prime sieve function
    from the helper module and will generate a list
    of primes up-till `limit` and return the sum of the list
    """
    return sum(prime_sieve(limit))


def main():
    print(sum_of_primes(2000000))


if __name__ == '__main__':
    main()
