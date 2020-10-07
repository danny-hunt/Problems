"""
Ghost is a two-person word game where players alternate appending letters to a word. 
The first person who spells out a word, or creates a prefix for which there is no 
possible continuation, loses. Here is a sample game:

Player 1: g
Player 2: h
Player 1: o
Player 2: s
Player 1: t [loses]
Given a dictionary of words, determine the letters the first player should start with, 
such that with optimal play they cannot lose.

For example, if the dictionary is ["cat", "calf", "dog", "bear"], 
the only winning start letter would be b.
"""

import string
import re

"""
for each letter in the alphabet, see whether that letter gives P1 a forced win
a letter gives a forced win iff there is no forced win for the second player in response 
AND there is a valid word with that starting letter sequence

function: determine winner from state A = current string + indication of who is to play

say player one = 0
    player two = 1
"""

alphabet = list(string.ascii_lowercase)
dictionary = ["cat", "calf", "dog", "bear"]
dictionary.sort()
dictionary_with_lengths = [ [x, len(x)] for x in dictionary]
print(dictionary_with_lengths)


def word_exists(string, dictionary = dictionary):
    # create regex pattern for string + [a-z]+ and check existence in dictionary
    pass



def who_wins(to_play = 0, string = ''):
    existing_length = len(string)
    if not word_exists(string):
        print(f'player {to_play} wins through lack of word')
        return 0
    
    #for
    

    



import string

dictionary = ["cat", "calf", "dog", "bear"]
dictionary.sort()

alphabet = list(string.ascii_lowercase)
#for letter in alphabet:
#    if 