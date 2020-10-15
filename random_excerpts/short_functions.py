# get prime factors of N

def prime_factors(N):
    divisor = 2
    factor_list = []
    while divisor <= N:
        if N % divisor == 0:
            factor_list.append(divisor)
            N /= divisor
        else:
            divisor += 1
    return factor_list

assert prime_factors(153) == [3,3,17]
assert prime_factors(120) == [2,2,2,3,5]

# identify a palindrome and output boolean
# only consider letters A-Z and ignore casing

import re

def is_palindrome(string):
    processed_string = ''.join(re.findall(r'[a-z]+', string.lower()))
    return processed_string == processed_string[::-1]

assert is_palindrome("a man, a plan, a canal, Panama!") == True
assert is_palindrome("and then there were none") == False

# sort the words in a string separated by spaces ignoring capitalisation in the sort

def sort_words(string):
    word_list = string.split(' ')
    lowered_list = [[word.lower(), index] for index, word in enumerate(word_list)]
    lowered_list.sort()
    output_list = [word_list[lowered_word[1]] for lowered_word in lowered_list]
    return output_list

assert sort_words("this is JUsT a Tribute ty") == ['a', 'is', 'JUsT', 'this', 'Tribute', 'ty']

# find the instances of a value in a list (note can be in a list in the list)

def find(list, value):
    counter = 0
    for element in list:
        if element == value:
            counter += 1
        else:
            try:
                counter += find(element, value)
            except:
                pass
    return counter

assert find([2, [2, 0]], 2) == 2

