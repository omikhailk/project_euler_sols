from helper import prime_sieve


def sum_of_primes(limit):
    """
    This function will use the Sieve of Eratosthenes
    from the helper module and will generate a list
    of primes uptill the limit that the user
    provides.

    Then it will return the sum of all those primes.
    """
    return sum(prime_sieve(limit))


print(sum_of_primes(2000000))
