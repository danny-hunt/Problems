"""
Soundex is an algorithm used to categorize phonetically, 
such that two names that sound alike but are spelled differently have the same representation.

Soundex maps every name to a string consisting of one letter and three numbers, like M460.

One version of the algorithm is as follows:

Remove consecutive consonants with the same sound (for example, change ck -> c).
Keep the first letter. The remaining steps only apply to the rest of the string.
Remove all vowels, including y, w, and h.
Replace all consonants with the following digits:
b, f, p, v → 1
c, g, j, k, q, s, x, z → 2
d, t → 3
l → 4
m, n → 5
r → 6
If you don't have three numbers yet, append zeros until you do. Keep the first three numbers.
Using this scheme, Jackson and Jaxen both map to J250.

Implement Soundex.
"""
consonants = {'b', 'c' ,'d', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z'}
vowels = {'a', 'e', 'i', 'o', 'u', 'y', 'w', 'h'}

mapping =  {'b': 1, 'f': 1, 'p': 1, 'v': 1, 
            'c': 2, 'g': 2, 'j': 2, 'k': 2, 'q': 2, 's': 2, 'x': 2, 'z': 2,
            'd': 3, 't': 3,
            'l': 4,
            'm': 5, 'n': 5,
            'r': 6}

def replace_consonants_with_digits(name, mapping=mapping):
    name = list(name)
    for index, letter in enumerate(name):
        if letter in consonants:
            name[index] = mapping[letter]
            print(letter)
    return name # this needs to actually be string for the name

def truncate_repeated_letters(name):
    truncated_name = [value for index, value in enumerate(name) if value != name[index-1]]
    return truncated_name




def soundex(name):
    name = name.lower()
    first_letter = str(name[0])
    name = replace_consonants_with_digits(name)
    truncated_name = truncate_repeated_letters(name)
    del(truncated_name[0])
    vowelless_name = [letter for letter in truncated_name if letter not in vowels]
    print(vowelless_name)
    print(first_letter)
    output = first_letter + ''.join(str(number) for number in vowelless_name[:3])
    while len(output) < 4:
        output += '0'
    output = output.upper()
    return output

print(replace_consonants_with_digits('Daniel'))
print(soundex('Damniel'))
print(soundex('alexandrpiu'))
