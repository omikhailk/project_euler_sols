"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""


from sys import exit


def palindrome_product_solver(digits):
    """
    Loops through two numbers each having
    digits equal to the `digits` variable.

    Then finds and returns the largest
    palindromic product of those two
    numbers.
    """
    if digits == 0:
        print("Exiting program.")
        exit
    else:
        start = 10 ** (digits - 1)
        end = 10 ** digits
    palindromes = set()
    for i in range(start, end):
        for w in range(i, end):
            if str(i * w) == str(i * w)[::-1]:
                palindromes.add(i * w)
    return max(palindromes)
            

def main():
    print(palindrome_product_solver(3))


if __name__ == "__main__":
    main()
