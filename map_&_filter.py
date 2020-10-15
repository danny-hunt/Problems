"""
Implement map and filter by only using lambda expressions and functools.reduce

map(func, seq)
map applies the function func to all the elements of the sequence seq and returns an iterator

filter(func, seq)
filter offers a way to filter out the elements of a sequence for which func returns True
"""

from functools import reduce


seq = [1, 2, 4, 5]
func = lambda x: x**2
print(list(map(func, seq)))

print(lambda x: func(x), seq)

#la