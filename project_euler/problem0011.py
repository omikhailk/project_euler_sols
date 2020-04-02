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


def top_to_bottom_diag_right(grid):
    diag_result = [[] for y in range(20)]
    searches_num = 17
    for i in range(20):
        for j in range(searches_num):
            prod = 1
            for g in range(0, 4):
                try:
                    prod *= int(grid[i + g][j + g])
                except IndexError as e:
                    pass
            diag_result[i].append(prod)
        diag_result[i] = max(diag_result[i])
    return max(diag_result)


def top_to_bottom_diag_left(grid):
    diag_result = [[] for y in range(20)]
    searches_num = 17
    for i in range(20):
        for j in range(searches_num):
            prod = 1
            for g in range(0, 4):
                try:
                    prod *= int(grid[i + g][j - g])
                except IndexError as e:
                    pass
            diag_result[i].append(prod)
        diag_result[i] = max(diag_result[i])
    return max(diag_result)


def main():
    data = get_grid("problem0011_input.txt")
    pass


if __name__ == '__main__':
    main()
