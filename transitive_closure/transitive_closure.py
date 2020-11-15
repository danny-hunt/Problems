"""
A classroom consists of N students, whose friendships can be represented in an adjacency list.
For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends with 6, and so on.

{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]}
Each student can be placed in a friend group, which can be defined as the transitive closure of that student's
friendship relations. In other words, this is the smallest set such that no student in the group has any friends
outside this group. For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.

Given a friendship list such as the one above, determine the number of friend groups in the class.
"""

import random

f_dict = {0: [1, 2],
          1: [0, 5],
          2: [0],
          3: [6],
          4: [],
          5: [1],
          6: [3]}


def create_friend_group(student, f_dict, friend_set = set()):
    # this is order n^2 in the number of friends in the friend group
    friend_set.add(student)
    for friend in f_dict[student]:
        if friend not in friend_set:
            friend_set = friend_set.union(create_friend_group(friend, f_dict, friend_set))
    return friend_set

counter = 0
students = set(range(7))
while f_dict:
    student = random.choice(list(students))
    print(student)
    new_set = set()
    clique = create_friend_group(student, f_dict, new_set)
    for student in clique:
        del f_dict[student]
        students.remove(student)
    counter += 1

print(counter)



