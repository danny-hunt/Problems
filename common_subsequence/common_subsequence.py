"""
Write a program that computes the length of the longest common subsequence of three given strings.
For example, given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious",
it should return 5, since the longest common subsequence is "eieio".
"""

# refzzzzz rezzzzzzzzz rez
# abcd cdef efab
# abbcbca bcbcba aabbcabc

# todo actually make this work

def reduce_words(word_list):
    reduced_words = []
    for index, word in enumerate(word_list):
        word_string = "".join(
            letter
            for letter in word
            if letter in word_list[0]
            and letter in word_list[1]
            and letter in word_list[2]
        )

        reduced_words.append(word_string)

    print(reduced_words)
    reduced_words.sort(key=len)
    return reduced_words


def longest_subsequence(reduced_words):
    possibles = {}
    lens = len(reduced_words[0]), len(reduced_words[1]), len(reduced_words[2])

    for i, letter in enumerate(reduced_words[0]):
        possible_word = ""
        j_index = 0
        k_index = 0

        if letter in reduced_words[1][j_index:] and letter in reduced_words[2][k_index:]:
            j_index += reduced_words[1][j_index:].find(letter) + 1
            k_index += reduced_words[2][j_index:].find(letter) + 1
            possible_word += letter
            recall(i+1, j_index, k_index, possible_word, possibles, reduced_words, lens)
        else:
            print(possible_word)
            possibles[possible_word] = len(possible_word)

    return possibles

def recall(i_index, j_index, k_index, possible_word, possible_list, reduced_words, lens):
    if i_index == lens[0] or j_index == lens[1] or k_index == lens[2]:
        possible_list[possible_word] = len(possible_word)
        return

    for i, letter in enumerate(reduced_words[0][i_index + 1:]):
        if letter in reduced_words[1][j_index+1:] and letter in reduced_words[2][k_index+1:]:
            print(i_index, j_index, k_index)
            j_index += reduced_words[1][j_index+1:].find(letter) + 1
            k_index += reduced_words[2][k_index+1:].find(letter) + 1
            possible_word += letter
            recall(i, j_index, k_index, possible_word, possible_list, reduced_words, lens)
        else:
            possible_list[possible_word] = len(possible_word)


print(longest_subsequence(reduce_words(['refzzzzz', 'rezzzzasfzzzzz', 'reeez'])))

# print(reduce_words(['refzzzzz', 'rezzzzasfzzzzz', 'reeez']))
