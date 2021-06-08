"""
What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""


from math import lcm


def smallest_multiple(limit):
    """
    Will return the smallest number that can be evenly divided
    by all the numbers from 1 to and including `limit`.
    """
    return lcm(*[i for i in range(1, limit + 1)])


def main():
    print(smallest_multiple(20))


if __name__ == '__main__':
    main()
