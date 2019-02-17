file_input = open("problem11_input.txt", "r")

nums_input = []

for line in file_input:
	nums_input.append(line.split(" "))

"""
Here we convert every element 
in every row of the list 
nums_input to a tuple.

And later we convert 
nums_input to a tuple 
also.
"""
for row in range(0, len(nums_input)):
	for element in range(0, len(nums_input[row])):
		nums_input[row][element] = int(nums_input[row][element])
	nums_input[row] = tuple(nums_input[row])

nums_input = tuple(nums_input)

def right_search():
	"""
	Multiplying the numbers
	left and right gives the same
	result
	"""
	row_result = [[] for z in range(20)]
	searches_per_row = 17
	for i in range(20):
		for w in range(searches_per_row):
			product = nums_input[i][w] * nums_input[i][w + 1] * nums_input[i][w + 2] * nums_input[i][w + 3]
			row_result[i].append(product)
		row_result[i] = max(row_result[i])
	print(row_result)

def up_search():
	"""
	Multiplying the numbers
	up and down will still
	give the same result
	"""
	column_result = [[] for z in range(20)]
	searches_per_column = 17
	for i in range(20):
		for w in range(searches_per_column):
			product = nums_input[w][i] * nums_input[w + 1][i] * nums_input[w + 2][i] * nums_input[w + 3][i]
			column_result[i].append(product)
		column_result[i] = max(column_result[i])
	print(column_result)


def diagonal_search():
	# I'm clueless
