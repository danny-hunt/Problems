"""
Given an array of numbers,
find the length of the longest increasing subsequence in the array.
subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
"""

from typing import List


input_array = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]


# go from number to number
# carry a list of subsequence length -> largest number in subsequence
# if the number is larger than any largest numbers then add a new subsequence
# (only if it's less than the existing size of that subsequence or if that subsequence doesn't exist)
# do this by iterating over our list in reverse


def find_subsequence_length(array: List[int]) -> int:
    current_longest = {0: min(array) - 1}

    for entry in array:
        new_current_longest = {}
        for largest in current_longest:
            if entry > current_longest[largest]:
                if largest + 1 in current_longest:
                    if entry < current_longest[largest + 1]:
                        new_current_longest[largest + 1] = entry
                else:
                    new_current_longest[largest + 1] = entry

        # this is all very clumsy - would be much better to iterate over a list in reverse instead
        for new in new_current_longest:
            if new < len(new_current_longest):
                current_longest[new] = min(new_current_longest[new], current_longest[new])
            else:
                current_longest[new] = new_current_longest[new]

    return max(current_longest.keys())

print(find_subsequence_length(input_array))

# O(n^2)
# Achievable in O(nlogn) with dynamic programming
