"""
Which starting number, under one million, produces the longest chain in the
Collatz sequence?
"""


from helper import collatz


def longest_iterations(num_limit):
    """
    Will use all numbers under `num_limit` and
    will return the number that causes the most iterations
    of the Collatz sequence.
    """
    iterations = [collatz(i) for i in range(1, num_limit)]
    return iterations.index(max(iterations))


def main():
    print(longest_iterations(1000000))


if __name__ == '__main__':
    main()
