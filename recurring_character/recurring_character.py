"""
Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""

from dis import dis

def find_recurring(string):
    # O(n) with storage space O(n) too
    check_set = set()
    for letter in string:
        if letter in check_set:
            return letter
        else:
            check_set.add(letter)
    return None

print(find_recurring("acbbac"))

def find_recurring_2(string):
    for index, letter in enumerate(string):
        if letter in string[index+1:]:
            return letter

    return None

print(find_recurring_2("acbbac"))
dis(find_recurring_2)
dis(find_recurring)

