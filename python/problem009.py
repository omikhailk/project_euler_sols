"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def pythagorean_triplets(sum_value):
    """
    Will find the three Pythagorean triplets
    whose sum will equal `sum_value`.

    Will then multiply the triplets and return them.
    """
    limit = sum_value + 1
    for x in range(1, limit):
        for y in range(x, limit):
            for z in range(y, limit):
                if x ** 2 + y ** 2 == z ** 2:
                    if x + y + z == sum_value:
                        return x * y * z


def main():
    print(pythagorean_triplets(1000))


if __name__ == '__main__':
    main()
