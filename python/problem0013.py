"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

The numbers are in `problem0013_input.txt`.
"""


def get_nums(file_path):
    """
    Reads every line from `file_path` and returns a list of the numbers.
    """
    num_list = []
    with open(file_path, 'r') as f:
        for line in f:
            num_list.append(int(line))
    return num_list


def digit_limited_sum(num_list, digit_limit):
    """
    Returns the sum of `num_list` to however many digits `digit_limit` is
    equal to.
    """
    digits_result = [i for i in str(sum(num_list))]
    return int(''.join(digits_result[:digit_limit]))


def main():
    numbers = get_nums('problem0013_input.txt')
    print(digit_limited_sum(numbers, 10))


if __name__ == '__main__':
    main()