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

def list_one_off(start_word, dictionary):
    one_step_words = []
    for word in dictionary:
        count = 0
        for x in range(len(word)):
            if word[x] != start_word[x]:
                count += 1
        if count == 1:
            one_step_words.append(word)
    return one_step_words

print(list_one_off("dog", dictionary))


        