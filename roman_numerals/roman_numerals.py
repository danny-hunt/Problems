"""
Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.

For the input XIV, for instance, you should return 14.
"""


roman_values = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

def to_decimal(roman):
    sum = 0
    for index, letter in enumerate(roman):
        negative = 1
        for new_letter in roman[index+1:]:
            if roman_values[new_letter] > roman_values[letter]:
                negative = -1
        sum += roman_values[letter] * negative
    return sum

print(to_decimal('XIV'))
print(to_decimal('MMMCDXLIV'))
