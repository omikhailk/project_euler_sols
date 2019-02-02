def largest_palindrome_product(digits):
	"""
	This will return the largest palindromic number
	made from the product of two N digit numbers.
	"""

	palindromes = []
	lower_bounds = 10 ** (digits - 1)
	upper_bounds = int("9" * digits)

	for i in range(upper_bounds, lower_bounds, -1):
		for w in range(i, lower_bounds, -1):
			number = str(i * w)
			if number == number[::-1]:
				palindromes.append(int(number))
			palindromes.sort()
			if len(palindromes) > 1:
				palindromes = [palindromes[-1]]
	return palindromes

print(largest_palindrome_product(3))