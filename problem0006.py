def sum_square_diff(limit_num):
    """
    This function will return the difference between
    the sum of the squares of the numbers in
    range(1, limit_num + 1), and the square of the sum of
    the numbers range(1, limit_num + 1).
    """
    square_of_sum = 0
    numbers_list = [i for i in range(1, limit_num + 1)]
    for number in numbers_list:
        square_of_sum += number
    square_of_sum = square_of_sum ** 2

    sum_of_squares = 0
    for number in numbers_list:
        sum_of_squares += number ** 2

    return square_of_sum - sum_of_squares


print(sum_square_diff(100))
