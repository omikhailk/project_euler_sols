"""
By considering the terms in the Fibonacci
sequence whose values do not exceed four
million, find the sum of the even-valued terms.
"""


from helper import fib, fib_term_from_value


def even_sum(limit):
    """
    Finds the sum of all of the even-valued terms
    in the fibonacci sequence which are below
    the `limit` number.
    """
    terms = [fib(i) for i in range(1, fib_term_from_value(limit)) if not fib(i) % 2]
    return sum(terms)
    

def main():
    print(even_sum(4000000))
    

if __name__ == '__main__':
    main()
