"""
Write an algorithm to justify text.
Given a sequence of words and an integer line length k,
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word.
Pad extra spaces when necessary so that each line has exactly length k.
Spaces should be distributed as equally as possible, with the extra spaces,
if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""

example_string = "this is an example input into the thingy; this word is sixteen characters long: abcdefghabcdefgh and so on"
example_input = example_string.split(" ")


def justify(words, k):
    justified = []
    words_to_add = []
    length_count = 0
    for word in words:
        length = len(word)
        if length_count == 0:
            result = length_count + length
        else:
            result = length_count + length + 1
        if result > k:
            justified.append(create_line(words_to_add, length_count, k))
            words_to_add = []
            words_to_add.append(word)
            length_count = length
        else:
            words_to_add.append(word)
            length_count = result
    if len(words_to_add) > 0:
        justified.append(create_line(words_to_add, length_count, k))

    return justified

import math

def create_line(words, length_count, k):
    if len(words) > 1:
        spaces = [0] * (len(words) - 1)

        number_of_spaces = k - length_count + len(spaces)
        counter = 0
        while number_of_spaces > 0:
            spaces[counter % (len(words)-1)] += 1
            number_of_spaces -= 1
            counter += 1

        return_string = ""
        for index, word in enumerate(words):
            if index > 0:
                return_string += " " * spaces[index - 1]
            return_string += word
    else:
        return_string = " " * math.ceil((k - length_count)/ 2) + words[0] + " " * math.floor((k - length_count)/ 2)
    return return_string

for word in justify(example_input, 16):
    print(word)
