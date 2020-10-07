"""
Given a start word, an end word, and a dictionary of valid words, 
find the shortest transformation sequence from start to end such that
only one letter is changed at each step of the sequence, and each transformed 
word exists in the dictionary. 
If there is no possible transformation, return null. 
Each word in the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", 
                   end = "cat", and 
                   dictionary = {"dot", "dop", "dat", "cat"},
return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, 
return null as there is no possible transformation from dog to cat.
"""

start = "dog"
end = "cat"
dictionary = {"dot", "dop", "dat", "cat"}
start_word_set = [start]
checked_words = set(start_word_set[0])
#dictionary.


def list_one_off(start_word_set, dictionary, checked_words = checked_words):
    one_step_words = []
    for starting_word in start_word_set:
        for possible_word in dictionary:
            count = 0
            for letter in range(len(possible_word)):
                if starting_word[letter] != possible_word[letter]:
                    count += 1
            if count == 1 and possible_word not in checked_words:
                one_step_words.append(possible_word)
    return one_step_words

print(list_one_off(start_word_set, dictionary))

def update_checked_words(newly_checked_words, checked_words_set):
    checked_words_set.add_contents_of(one_step_words)

#set might need to be replaced by a dict so that we can track the path to the answer
#atm all we can do is check whether there is a path


        