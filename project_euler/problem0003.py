"""
What is the largest prime factor of the number 600851475143?
"""


def biggest_prime_factor(num):
    """
    Returns the largest prime factor of `num`.

    Uses the trial division method.
    """
    prime_factors = []
    trial_factor = 2
    while num != 1:
        if num % trial_factor == 0:
            prime_factors.append(trial_factor)
            num /= trial_factor
        else:
            trial_factor += 1
        if len(prime_factors) > 1:
            prime_factors = [prime_factors[-1]]
    return prime_factors


def main():
    print(biggest_prime_factor(600851475143))


if __name__ == '__main__':
    main()
