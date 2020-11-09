"""
Given a string of words delimited by spaces, reverse the words in string.
For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?
"""


def first_reverse(string):
    word_list = string.split(" ")
    word_list.reverse()
    return " ".join(word_list).strip()


print(first_reverse("this is the word list a thing"))


def second_reverse(character_list):
    character_list.reverse()
    head = 0
    last_word_start = 0
    while head < len(character_list):
        if character_list[head] == " ":
            character_list[last_word_start:head] = character_list[last_word_start:head][::-1]
            last_word_start = head + 1
        head += 1
    character_list[last_word_start:head] = character_list[last_word_start:head][::-1]

    return character_list


print(second_reverse(list("this is the word list a thing")))
