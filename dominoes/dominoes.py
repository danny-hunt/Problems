"""
You are given an string representing the initial conditions of some dominoes. 
Each element can take one of three values:

L, meaning the domino has just been pushed to the left,
R, meaning the domino has just been pushed to the right, or
., meaning the domino is standing still.
Determine the orientation of each tile when the dominoes stop falling. 
Note that if a domino receives a force from the left and right side simultaneously, 
it will remain upright.

For example, given the string .L.R....L, you should return LL.RRRLLL

Given the string ..R...L.L, you should return ..RR.LLLL
"""


def calculate(dominoes):
    index = 0
    current_state = dominoes[index]
    to_resolve = []
    for index in range(len(dominoes)):
        if dominoes[index] == '.':
            to_resolve.append(index)
        if dominoes[index] == 'R':
            current_state = 'R'
            to_resolve = [index]
        if dominoes[index] == 'L':
            if current_state == '.':
                for ii in to_resolve:
                    dominoes[ii] = 'L'
            if current_state == 'R':
                for i, value in enumerate(to_resolve):
                    if i < len(to_resolve) // 2:
                        dominoes[value] = 'R'
                    if i > len(to_resolve) // 2:
                        dominoes[value] = 'L'
            to_resolve = []
            current_state = '.'
    return ''.join(dominoes)


dominoes = list(".LR...L.L..R...L.L..R...L.L..R...L.L")
print(calculate(dominoes))





