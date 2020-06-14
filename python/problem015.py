"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""


# Allows us to calculate nCr
from math import comb


def main():
    """
    This is a lattice paths problem. We want all the combinations of all the possible paths
    from the origin (i.e the top left corner) to the bottom right corner.

    Searching this up on Wikipedia, I found that the solution for this problem is a well known
    result in combinatorics. The solution is (2n)C(n) [2n choose n], where n is the coordinate
    of the ending square (which is 20 in this case).

    So the solution is 40C20.
    """
    print(comb(40, 20))


if __name__ == '__main__':
    main()
