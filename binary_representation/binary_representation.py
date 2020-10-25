"""
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
"""
def longest_ones(n):
    power_of_two = 1
    largest_number_of_ones = 0
    current_number_of_ones = 0

    n % 2 