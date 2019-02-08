import time

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

def prime_factorisation_primality(num, trivial):
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
	if trivial == True:
		prime_factors.append(1)
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

def prime_sieve(limit):
	"""
	This function is an algorithm for finding
	the primes upto a certain number.

	This version of the algorithm is not the most optimised
	one.

	The algorithm is called 'The Sieve of
	Eratosthenes'
	"""
	number_list = [[i, True] for i in range(3, limit + 1, 2)]
	current_p = 3
	result_primes = [2]
	marked_nums = []
	while current_p ** 2 <= limit:
		for i in number_list:
			if i[0] % current_p == 0 and i[0] != current_p:
				i[1] = False
		for i in number_list:
			if i[0] > current_p and i[1] == True:
				current_p = i[0]
				break
	for i in number_list:
		if i[1] == True:
			result_primes.append(i[0])
	return result_primes

def t_num_generator(term_range):
	"""
	Will generate the triangular numbers uptill term_range
	in a list.
	"""
	result = [(i * (i + 1) / 2) for i in range(0, term_range)]
	return result

if __name__ == "__main__":
	pass