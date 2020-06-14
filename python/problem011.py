"""
What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20×20 grid?
"""


from math import prod


def get_grid(numbers):
    with open(numbers, "r") as f:
        data = []
        for line in f:
            data.append(line.split())
    return data


def horizontal_search(grid):
    """
    Returns the largest product of 4 adjacent numbers when
    moving along the grid horizontally.
    """
    result = [0]
    for row_index in range(0, len(grid)):
        result = [max(result)]
        # Shortens the `result` list every row to save space
        for index in range(0, len(grid[row_index]) - 4):
            adj_nums = [int(num) for num in grid[row_index][index:index + 4]]
            # Converts the 4 adjacent numbers in every row to a list with the
            # numbers as integers
            result.append(prod(adj_nums))
    return max(result)


def vertical_search(grid):
    """
    Returns the largest product of 4 adjacent numbers when
    moving along the grid vertically.
    """
    result = [0]
    grid = list(zip(*grid))
    # Transposes the list, so that all the vertical numbers are in rows
    for row_index in range(0, len(grid)):
        result = [max(result)]
        for index in range(0, len(grid[row_index]) - 4):
            adj_nums = [int(num) for num in grid[row_index][index:index + 4]]
            result.append(prod(adj_nums))
    return max(result)


def left_to_right_diag(grid):
    """
   Returns the largest product in the grid of 4 adjacent numbers
   in a diagonal (from left to right).
    """
    diag = []
    for col in range(0, len(grid), 4):
        four_adj_nums = []
        for row in range(0, len(grid) - 3):
            for i in range(0, 4):
                four_adj_nums.append(grid[col + i][row + i])
        diag.append(four_adj_nums)
    nums = []
    for index in range(0, len(diag)):
        for sub in range(0, len(diag[index]) - 4, 4):
            nums.append([int(i) for i in diag[index][sub:sub+4]])
    products = [prod(i) for i in nums]
    return max(products)


def right_to_left_diag(grid):
    """
    Returns the largest product in the grid of 4 adjacent numbers
    in a diagonal (from right to left).
    """
    diag = []
    for col in range(len(grid) - 1, 0, -4):
        four_adj_nums = []
        for row in range(0, len(grid) - 3):
            for i in range(0, 4):
                four_adj_nums.append(grid[col - i][row + i])
        diag.append(four_adj_nums)
    nums = []
    for index in range(0, len(diag)):
        for sub in range(0, len(diag[index]) - 4, 4):
            nums.append([int(i) for i in diag[index][sub:sub+4]])
    products = [prod(i) for i in nums]
    return max(products)


def main():
    data = get_grid("problem0011_input.txt")
    print(horizontal_search(data))
    print(vertical_search(data))
    print(right_to_left_diag(data))
    print(left_to_right_diag(data))


if __name__ == '__main__':
    main()
