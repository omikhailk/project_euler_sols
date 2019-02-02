def fib(term):
	if term == 1:
		return 1
	if term == 2:
		return 2
	elif term > 1:
		return fib(term - 1) + fib(term - 2)

def even_valued_terms(limit):
	even_values = []
	i = 1
	while fib(i) <= limit:
		if fib(i) % 2 == 0:
			even_values.append(fib(i))
		i += 1
	return sum(even_values)

print(even_valued_terms(4000000))