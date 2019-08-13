def three_or_five_multiples(limit):
	"""
	This function will find the sum of all of the
	multiples of 3 or 5 which are below the limit.
	"""
	multiples = []
	for i in range(1, limit):
		if i % 3 == 0 or i % 5 == 0:
			multiples.append(i)
	return sum(multiples)

print(three_or_five_multiples(1000))
