from math import factorial

result = 0
for digit in str(factorial(100)):
    result += int(digit)

print(result)
