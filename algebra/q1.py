"""
Let m be a positive integer and let a0, a1, ..., am be a sequence of reals
such that a0 = 37, a1= 72, am=0 and ak+1 = ak-1 -3/ak  for k = 1, 2, ..., m-1
Find m
"""

input_list = [37, 72]

def complete_list(input_list):
    next = input_list[-2] - 3/input_list[-1]
    input_list.append(next)

while input_list[-1] > 0.1:
    complete_list(input_list)

print(len(input_list))


