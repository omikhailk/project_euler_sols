"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and"
when writing out numbers is in compliance with British usage.
"""


num_to_word = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'onehundred',
    200: 'twohundred',
    300: 'threehundred',
    400: 'fourhundred',
    500: 'fivehundred',
    600: 'sixhundred',
    700: 'sevenhundred',
    800: 'eighthundred',
    900: 'ninehundred',
    1000: 'onethousand'
}


def number_to_word(num):
    num_str = str(num)
    # Handles special cases
    if num in num_to_word.keys():
        return len(num_to_word[int(num_str)])
        # return num_to_word[int(num_str)]
    if len(num_str) == 1:
        final_str = num_to_word[int(num_str)]
    elif len(num_str) == 2:
        tens = int(num_str[0]) * 10
        ones = int(num_str[1])
        if ones not in num_to_word.keys():
            final_str = num_to_word[tens]
        else:
            final_str = num_to_word[tens] + num_to_word[ones]
    else:
        hundreds = int(num_str[0]) * 100
        tens = int(num_str[1]) * 10
        ones = int(num_str[2])
        if int(num_str[1:]) in num_to_word.keys():
            final_str = f'{num_to_word[hundreds]}and{num_to_word[int(num_str[1:])]}'
        elif ones not in num_to_word.keys():
            final_str = f'{num_to_word[hundreds]}and{num_to_word[tens]}'
        elif tens not in num_to_word.keys():
            final_str = f'{num_to_word[hundreds]}and{num_to_word[ones]}'
        else:
            final_str = f'{num_to_word[hundreds]}and{num_to_word[tens]}{num_to_word[ones]}'
    return len(final_str)

total = 0
for i in range(1, 1001):
    total += number_to_word(i)
print(total)

