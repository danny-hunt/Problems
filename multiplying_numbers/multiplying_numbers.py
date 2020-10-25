"""
Given a list of integers, return the largest product
that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2],
we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""


def largest_product(integers):
    if len(integers) == 3:
        return integers[0] * integers[1] * integers[2]

    positives = []
    negatives = []
    for number in integers:
        if number > 0:
            add_to_list(number, positives)
        else:
            add_to_list(number, negatives, 2)

    if len(integers) == 4:
        if len(negatives) == 2:
            return negatives[0] * negatives[1] * positives[1]
        else:
            return positives[0] * positives[1] * positives[2]

    option_one = positives[0] * positives[1] * positives[2]
    option_two = positives[2] * negatives[0] * negatives[1]
    return max(option_one, option_two)


def add_to_list(integer, list, list_length=3):
    if len(list) < list_length:
        list.append(integer)
        list.sort()
    else:
        for index in range(list_length):
            if abs(integer) > abs(list[index]):
                list.pop(1)
                list.append(integer)
                list.sort()


print(largest_product([1, 2, 3, 4, 5, 6, 7, -6, -8]))
print(largest_product([2,3,-4,3]))
print(largest_product([-1, 2, 3]))
