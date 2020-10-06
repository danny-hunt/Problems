"""
In academia, the h-index is a metric used to calculate the impact of a researcher's papers. 
It is calculated as follows:

A researcher has index h if at least h of her N papers have h citations each. 
If there are multiple h satisfying this formula, the maximum is chosen.

For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5]. 
Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.

Given a list of paper citations of a researcher, calculate their h-index.
"""
import copy

citations_list = [5, 3, 0, 1, 5, 6, 7]


def h_index(citations_list):
    c = copy.copy(citations_list)
    c.sort()
    print(c)
    current_h = 0
    number_of_papers = len(c)
    for index, value in enumerate(c):
        while value <= number_of_papers - index and current_h <= value:
            current_h += 1
    return current_h

print(h_index(citations_list))

### now attempting to solve the problem without sorting/passing through the list multiple times
"""
stack = {}
for x in citations_list:
    if x in stack.keys():
        
"""