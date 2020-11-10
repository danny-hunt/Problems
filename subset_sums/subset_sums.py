"""
Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.
"""

"""
1 -> 1
1,2 -> 3
1,2,3 -> 6
1,2,3,4 -> 10
n(n+1)/2

1,2,3,4,11,22
"""

def smallest_missing(array):
    current_sum = 0
    for number in array:
        if number > current_sum + 1:
            return current_sum + 1
        else:
            current_sum += number
    return current_sum + 1

print(smallest_missing([1, 2, 3, 10]))
print(smallest_missing([1,2,3,4,8,19,37,75]))

