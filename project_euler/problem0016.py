"""
What is the sum of the digits of the number 21000?
"""


result = 0
for digit in str(2 ** 1000):
    result += int(digit)

print(result)
