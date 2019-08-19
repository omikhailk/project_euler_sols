def smallest_multiple(num_limit):
    """
    This function will return the smallest
    number that can be evenly divided by all
    the numbers from 1 to and including num_limit.
    """
    numbers = [i for i in range(1, num_limit + 1)]
    starting_num = 2

    while True:
        for case in numbers:
            if starting_num % case == 0:
                if case == num_limit:
                    return starting_num
            else:
                break
        starting_num += 1
        continue


print(smallest_multiple(20))
