"""
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_of_multiples(limit):
    """
    This function will find the sum of all of the
    multiples of 3 or 5 which are below the limit.
    """
    multiples = [i for i in range(1, limit) if not (i % 3 and i % 5)]
    return sum(multiples)


def main():
    print(sum_of_multiples(1000))


if __name__ == '__main__':
    main()
