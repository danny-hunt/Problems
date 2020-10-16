"""
Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.
"""
import random

def reverze(list, i, j):
    if i > 0 and j < len(list) - 1:
        return list[:i] + list[j:i-1:-1] + list[j+1:]
    elif i == 0:
        if j == len(list) - 1:
            return list.reverse()
        else:
            #finish this part at some point
            pass


point = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(point[:0])
print(point[1])
print(reverze(point, 0, 2))
assert reverze(point, 5, 8) == [0, 1, 2, 3, 4, 8, 7, 6, 5, 9, 10]
assert reverze(point, 1, 2) == [0, 2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
assert reverze(point, 0, 2) == [2, 1, 0, 3, 4, 5, 6, 7, 8, 9, 10]

assert reverze(point, 0, 1) == [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10]



def bubble(list):
    counter = 1
    while counter != 0:
        counter = 0
        for index in range(len(list) - 1):
            if list[index] > list[index+1]:
                list = reverze(list, index, index+1)
                counter += 1
        #print(list)
    return list

starting_list = list(range(10))
random.shuffle(starting_list)

print(bubble(starting_list))