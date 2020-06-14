"""
Find the sum of the digits in the number 100!
"""


from math import factorial
from helper import get_digits


def main():
    print(sum(get_digits(factorial(100))))


if __name__ == "__main__":
    main()
