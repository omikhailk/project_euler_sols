"""
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


def sum_square_diff(limit_num):
    """
    This function will return the difference between
    the sum of the squares and the square of the sums of the numbers
    in the range 1 <= num <= limit_num
    """
    square_of_sum = sum([i for i in range(1, limit_num + 1)])
    square_of_sum **= 2

    sum_of_squares = sum([i ** 2 for i in range(1, limit_num + 1)])

    return square_of_sum - sum_of_squares


def main():
    print(sum_square_diff(100))


if __name__ == '__main__':
    main()
