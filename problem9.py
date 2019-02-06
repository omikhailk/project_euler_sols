def pythagorean_triplets(sum_value):
	"""
	This program will find the three Pythagorean
	triplets whose sum will equal sum_value.

	Then the program will multiply the three
	triplets to get the product xyz. Which it
	will output.
	"""
	limits = 1001
	for x in range(1, limits):
		for y in range(x, limits):
			for z in range(y, limits):
				if x ** 2 + y ** 2 == z ** 2:
					if x + y + z == sum_value:
						return x * y * z

print(pythagorean_triplets(1000))