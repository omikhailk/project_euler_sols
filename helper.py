"""
This file is a helper module which will contain
important functions which I may use again in
other problems
"""

def fib(term):
	"""
	This is a recursive fibonacci function.
	"""
	if term == 1:
		return 1
	if term == 2:
		return 2
	elif term > 1:
		return fib(term - 1) + fib(term - 2)

def prime_factorisation_primality(num):
	"""
	This function will return the prime factors
	and the primality of a given number.
	"""
	prime_factors = []
	trial_factor = 2
	if num == 1:
		primality = False
	else:
		primality = True
	while num != 1:
		if num % trial_factor == 0:
			prime_factors.append(trial_factor)
			num /= trial_factor
		else:
			trial_factor += 1
		if len(prime_factors) > 1:
			primality = False
	return [prime_factors, primality]

def prime_finder(index):
	"""
	This program will find the prime with the index
	you want.
	"""
	count = 1
	current_prime = 2
	current_number = 3
	while count < index:
		if prime_factorisation_primality(current_number)[1] == True:
			count += 1
			current_prime = current_number
		current_number += 2
	return current_prime

if __name__ == "__main__":
	pass