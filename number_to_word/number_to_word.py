"""
Given a mapping of digits to letters (as in a phone number), and a digit string,
return all possible letters the number could represent.
You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return
[“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""

phone_mapping = {
    "2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'],
    "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']
}

digit_string = "4245283545236892"

print(len(digit_string))

print(3**len(digit_string))

def possible_words(digit_string, starting_list = ['']):
    current_list = starting_list.copy()
    for index, digit in enumerate(digit_string):
        new_list = []
        for letter in phone_mapping[digit]:
            for word in current_list:
                new_list.append(word + letter)
        current_list = new_list.copy()
    print(current_list[0], current_list[-1])
    return current_list

print(possible_words("232"))

print(len(possible_words(digit_string)))
