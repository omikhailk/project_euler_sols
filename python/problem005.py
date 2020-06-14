"""
What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""


def smallest_multiple(limit):
    """
    Will return the smallest number that can be evenly divided
    by all the numbers from 1 to and including `limit`.
    """
    numbers = [i for i in range(1, limit + 1)]
    starting_num = 2

    while True:
        for case in numbers:
            if not starting_num % case:
                if case == limit:
                    return starting_num
            else:
                break
        starting_num += 1
        continue


def main():
    print(smallest_multiple(20))


if __name__ == '__main__':
    main()
