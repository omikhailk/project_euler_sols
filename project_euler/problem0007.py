def is_prime(num):
    trial_factor = 2
    primes = []
    while num != 1:
        if num % trial_factor == 0:
            primes.append(trial_factor)
            num /= trial_factor
        else:
            trial_factor += 1
        if len(primes) > 1:
            return False
    return True


def prime_finder(index):
    """
    Will find the Nth prime, where the value
    of N is the index parameter.
    """
    count = 1
    current_prime = 2
    current_number = 3
    while count < index:
        if is_prime(current_number):
            count += 1
            current_prime = current_number
        current_number += 2
    return current_prime


def main():
    print(prime_finder(10001))


if __name__ == '__main__':
    main()
