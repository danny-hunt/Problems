"""
Write a Python function to check whether two strings are anagrams.
Do a version with and without sorting.
Why might you want a function that can do this without sorting?
"""


def is_anagram_with_sorting(string_1, string_2):
    first_string, second_string = list(string_1), list(string_2)
    first_string.sort()
    second_string.sort()

    return first_string == second_string


assert is_anagram_with_sorting("trade", "tread")
print(is_anagram_with_sorting("trade", "trader"))


def is_anagram_without_sorting(string_1, string_2):
    first_string = {}
    for letter in string_1:
        if letter in first_string:
            first_string[letter] += 1
        else:
            first_string[letter] = 1

    for letter in string_2:
        if letter not in first_string:
            return False

        first_string[letter] -= 1
        if first_string[letter] == 0:
            del first_string[letter]
    return not first_string


assert is_anagram_without_sorting("trade", "tread")
print(is_anagram_without_sorting("trade", "trader"))

"""
The version without sorting runs in O(n) time where n is sum of the string lengths. Each letter is visited only once
and has constant actions done to it. Sorting is in O(nlogn) time which is slower for longer words. 
"""