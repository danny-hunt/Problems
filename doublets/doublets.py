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
dictionary = {"dot", "dop", "dat", "cat", "fro"}
start_word_set = [start]
checked_words = {start}


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


def add_contents_of(set, additions):
    for word in additions:
        if word not in set:
            set.add(word)


def update_checked_words(newly_checked_words, checked_words_set=checked_words):
    add_contents_of(checked_words_set, newly_checked_words)


while end not in checked_words:
    new_words = list_one_off(start_word_set, dictionary)
    update_checked_words(new_words)
    start_word_set = new_words
    print(checked_words)


# at the moment, this only terminates if there is a path to the target word
# it also would error if the dictionary contains words of different sizes