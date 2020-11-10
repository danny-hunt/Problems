"""
A step word is formed by taking a given word, adding a letter, and anagramming the result.
For example, starting with the word "APPLE", you can add an "A" and anagram to get "APPEAL".

Given a dictionary of words and an input word, create a function that returns all valid step words.
"""
import json
from string import ascii_lowercase

# 26 * 6!


dictionary_of_words = ["help", "heap", "hep", "pleh", "hepa"]
start_word = "hep"


def try_words(word_list, start_word):
    dictionary = set(word_list)
    output = []
    for index in range(len(start_word)+1):
        for letter in ascii_lowercase:
            word_to_try = list(start_word.strip())
            word_to_try.insert(index, letter)
            string_to_try = "".join(word_to_try)
            print(string_to_try)
            if string_to_try in dictionary:
                output.append(string_to_try)
    return output

print(try_words(dictionary_of_words, start_word))



def step_words(word_list, start_word):
    reduced_words = {}
    for word in word_list:
        reduction = word_reduce(word)
        if reduction in reduced_words:
            reduced_words[reduction].append(word)
        else:
            reduced_words[reduction] = [word]
    print(reduced_words)
    step_words = []

    search_reduction = word_reduce(start_word, "dict")
    for letter in ascii_lowercase:
        if letter in search_reduction:
            search_reduction[letter] += 1
        else:
            search_reduction[letter] = 1
        if json.dumps(search_reduction) in reduced_words:

            step_words.extend(reduced_words[search_reduction])

    return step_words


def word_reduce(word, typo="string"):
    letter_dict = {}
    for letter in word:
        if letter in [l[0] for l in letter_dict]:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    if typo == "string":
        return json.dumps(letter_dict)
    else:
        return letter_dict


print(step_words(dictionary_of_words, start_word))