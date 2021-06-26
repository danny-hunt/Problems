"""
Given a multiset of integers,
return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true,
since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up
into two subsets that add up to the same sum.
"""

def partitionable(multiset):
    size = sum(multiset)
    if size % 2 == 1:
        return False
    multilist = list(multiset)
    # initialise table
    array = [(len(multiset) + 1) * [0]] * ((size + 2) // 2)
    print(len(array))

    for x in array:
        x[0] = False
    array[0] = [True] * (len(multiset) + 1)
    print(array)


example_set = (15, 5, 20, 10, 35, 15, 10)
print(example_set)

print(partitionable(example_set))