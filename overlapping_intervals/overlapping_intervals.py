"""
Given a collection of intervals, find the minimum number of intervals
 you need to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8),
return 1 as the last interval can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.
"""

from random import randint

intervals = [(7,9), (2,4), (2,6), (2,5), (5,8)]
intervals = [(7,9), (2,4), (2,6), (2,5), (5,8)]


def create_random_intervals():
    interval_list = []
    for _ in range(10):
        start_point = randint(0,10)
        interval_list.append((start_point, start_point + randint(1,4)))
    interval_list.sort()
    return interval_list


rand_1 = create_random_intervals()
rand_2 = create_random_intervals()


"""
-------||||||------------
-----||||------|||||----|||--
----||||||----||||---||--


--||||||----  X 1
--|||||-----  X 2
---|||------  
-----||||||-  X 3
-----||||---  X 4

Approach used is to:
1. sort the list of intervals by their start_points
2. find the interval with the first end_point
3. remove it and all intervals overlapping with this interval (counting the overlaps)
4. repeat with the new interval list

This approach is O(nlogn) due to the sort.
With hindsight sorting by end point might have been a little neater
"""


intervals.sort()
print(intervals)


def resolve_first_endpoint(intervals):
    earliest_endpoint = 100
    earliest_interval_index = -1
    for index, interval in enumerate(intervals):
        if interval[1] < earliest_endpoint:
            earliest_endpoint = interval[1]
            earliest_interval_index = index
        elif interval[0] < earliest_endpoint:
            earliest_interval_index = index
    new_list = intervals[(earliest_interval_index+1):]
    return earliest_interval_index, new_list


def calculate_removals(intervals):
    counter = 0
    while len(intervals) > 1:
        increment, intervals = resolve_first_endpoint(intervals)
        print(f'increment is {increment} and intervals is {intervals}')
        counter += increment
    return counter

print(rand_1)
print(calculate_removals(rand_1))
print(rand_2)
print(calculate_removals(rand_2))