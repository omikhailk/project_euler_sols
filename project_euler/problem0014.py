"""
Which starting number, under one million, produces the longest chain in the
Collatz sequence?
"""


def collatz(num):
    original_num = num
    iterations = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        iterations += 1
    return (original_num, iterations)


def main():
    results = []
    start_num = 2
    while start_num < 1000000:
        results.append(collatz(start_num))
        start_num += 1

    max_iter = 1
    for i in results:
        if i[1] > max_iter:
            max_iter = i[1]

    for i in results:
        if i[1] == max_iter:
            print(i[0])


if __name__ == '__main__':
    main()
