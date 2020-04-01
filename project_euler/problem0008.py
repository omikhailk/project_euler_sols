"""
Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?
"""


from math import prod


def get_digits(text_file):
    """
    Reads `text_file`, adds each line to a list
    called `grid`, then flattens it and returns the whole list
    in `line_nums`.
    """
    with open(text_file, "r") as data:
        grid = [line.strip() for line in data]
    line_nums = [num for sublist in grid for num in sublist]
    # Flattens the 2D list
    return line_nums


def greatest_product(line_nums):
    """
    Takes `line_nums`, makes substrings of 13 digits which are then converted
    into individual integers, which are multiplied to form a product which is
    added to `result`. The product with the highest value is then returned
    """
    result = []
    for index in range(0, len(line_nums) - 13):
        # Uses `len(line_nums) - 13` as we only want 13 adjacent digits
        # at a time
        adj_digits = [int(num) for num in line_nums[index:index + 13]]
        # Takes a substring of 13 numbers and then converts that to a list
        # which each number is an integer
        result.append(prod(adj_digits))
    return max(result)


def main():
    print(greatest_product(get_digits("problem0008_input.txt")))


if __name__ == '__main__':
    main()
