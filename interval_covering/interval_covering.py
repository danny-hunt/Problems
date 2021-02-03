"""Given a set of closed intervals, find the smallest set of numbers that covers all the intervals.
If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9],
one set of numbers that covers all these intervals is {3, 6}.
"""


def smallest_cover(intervals):
    smallest_right_edge = intervals[0][1]
    largest_left_edge = intervals[0][0]

    for interval in intervals:
        if interval[1] < smallest_right_edge:
            smallest_right_edge = interval[1]
        if interval[0] > largest_left_edge:
            largest_left_edge = interval[0]

    return (smallest_right_edge, largest_left_edge)


print(smallest_cover([[0, 3], [2, 6], [3, 4], [6, 9]]))
