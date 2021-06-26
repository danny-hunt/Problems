"""
Given an unsorted array, in which all elements are distinct,
find a "peak" element in O(log N) time.

An element is considered a peak if it is greater than both its left and right neighbors.
It is guaranteed that the first and last elements are lower than all others.
"""
import random
from typing import List


def get_middle_index(lower_index: int, upper_index: int) -> int:
    return (upper_index + lower_index) // 2


def find_peak(array: List[int]) -> int:
    if len(array) == 1:
        return array[0]
    lower_index = 0
    upper_index = len(array) - 1
    middle_index = get_middle_index(lower_index, upper_index)
    if array[middle_index - 1] >= array[middle_index]:
        return find_peak(array[lower_index:middle_index + 1])

    if array[middle_index] > array[middle_index + 1]:
        return array[middle_index]
    else:
        return find_peak(array[middle_index:upper_index + 1])


def test_this(n: int) -> None:
    for _ in range(n):
        x = list(range(10))
        random.shuffle(x)
        x.insert(0, -1)
        x.append(-1)

        peak_index = x.index(find_peak(x))
        if x[peak_index - 1] < x[peak_index] and x[peak_index + 1] < x[peak_index]:
            print("TRUE")
        else:
            raise ArithmeticError("this is wrong")

test_this(10000)

