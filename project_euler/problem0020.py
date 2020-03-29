"""
Find the sum of the digits in the number 100!
"""


from math import factorial

result = 0
for digit in str(factorial(100)):
    result += int(digit)

print(result)
