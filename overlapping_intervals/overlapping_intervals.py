"""
Given a collection of intervals, find the minimum number of intervals
 you need to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8),
return 1 as the last interval can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.
"""

intervals = [(7,9), (2,4), (5,8)]
"""
-------||||||------------
-----||||------|||||----|||--
----||||||----||||---||--


--||||||----  X 1
--|||||-----  X 2
---|||------  
-----||||||-  X 3
-----||||---  X 4
"""

intervals.sort()

def resolve_first_interval(intervals):

    for index, interval in intervals:
        for other_intervals in intervals[(index+1):]:
            while other_intervals[1]<


for index, interval in enumerate(intervals):
    if interval[1] <