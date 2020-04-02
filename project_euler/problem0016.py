"""
What is the sum of the digits of the number 2 ** 1000?
"""


from helper import get_digits


def main():
    print(sum(get_digits(2 ** 1000)))


if __name__ == "__main__":
    main()
