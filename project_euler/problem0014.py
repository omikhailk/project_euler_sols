"""
Which starting number, under one million, produces the longest chain in the
Collatz sequence?
"""


def collatz(num):
    """
    Will use `num` to perform the Collatz sequence.

    Will return `num` and how many iterations it carried out.
    """
    original = num
    iterations = 1
    while num != 1:
        if not num % 2:
            num /= 2
        else:
            num = 3 * num + 1
        iterations += 1
    return original, iterations


def longest_iterations(num_limit):
    """
    Will use all numbers under `num_limit` and
    will return the number that causes the most iterations
    of the Collatz sequence.
    """
    iterations = [collatz(i)[1] for i in range(1, num_limit)]
    return iterations.index(max(iterations))


def main():
    print(longest_iterations(1000000))


if __name__ == '__main__':
    main()
