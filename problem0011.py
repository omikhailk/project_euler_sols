data = []

with open("problem0011_input.txt", "r") as f:
    for line in f:
        data.append(line.split())


def right_search(grid):
    row_result = [[] for y in range(20)]
    searches_num = 17
    for i in range(20):
        for j in range(searches_num):
            prod = 1
            for g in range(0, 4):
                prod *= int(grid[i][j + g])
            row_result[i].append(prod)
        row_result[i] = max(row_result[i])
    return max(row_result)


def up_search(grid):
    column_result = [[] for y in range(20)]
    searches_num = 17
    for i in range(20):
        for j in range(searches_num):
            prod = 1
            for g in range(0, 4):
                prod *= int(grid[j + g][i])
            column_result[i].append(prod)
        column_result[i] = max(column_result[i])
    return max(column_result)


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
    print(right_search(data))
    print(up_search(data))
    print(top_to_bottom_diag_right(data))
    print(top_to_bottom_diag_left(data))


if __name__ == '__main__':
    main()
