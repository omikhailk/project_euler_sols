"""
By considering the terms in the Fibonacci
sequence whose values do not exceed four
million, find the sum of the even-valued terms.
"""


from helper import fib, golden_ratio
from math import floor, log


def index_limit_det(limit):
    """
    Determines the term which was responsible for
    the (`limit` number)'s fibonacci value.
    The formula used can be found on:
    https://bit.ly/2p3Ectu
    """
    
    return floor(log((limit * (5 ** 0.5) + 0.5), golden_ratio))


def even_sum(limit):
    """
    Finds the sum of all of the even-valued terms
    in the fibonacci sequence which are below
    the `limit` number.
    """

    terms = [fib(i) for i in range(1, index_limit_det(limit)) if not fib(i) % 2]
    return sum(terms)
    

def main():
    print(even_sum(4000000))
    

if __name__ == '__main__':
    main()
