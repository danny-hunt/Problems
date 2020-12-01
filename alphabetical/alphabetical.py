"""
You come across a dictionary of sorted words in a language you've never seen before.
Write a program that returns the correct order of letters in this language.

For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'],
you should return ['x', 'z', 'w', 'y'].

abc abd eaf

"""


def compare_words(word_one, word_two, letter_order):
    for i in range(len(word_one)):
        if word_one[i] != word_two[i]:
            letter_order.add((word_one[i], word_two[i]))
            break


base_dictionary = ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']


def determine_order(dictionary):
    order = set()
    for i in range(len(base_dictionary) - 1):
        compare_words(base_dictionary[i], base_dictionary[i+1], order)

    # order now gives the pairwise comparisons
    # these still need to be turned into an example of a topological ordering


determine_order(base_dictionary)


