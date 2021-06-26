"""
Given an iterator with methods next() and hasNext(), create a wrapper iterator,
PeekableInterface, which also implements peek().
peek shows the next element that would be returned on next().

Here is the interface:

class PeekableInterface(object):
    def __init__(self, iterator):
        pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass
"""

# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekableInterface(object):
    def __init__(self, iterator):
        self.has_peeked = False
        self.peeked_value = None
        self.iterator = iterator

    def peek(self):
        if not self.has_peeked:
            self.has_peeked = True
            return self.iterator.next()

    def next(self):
        if not self.has_peeked:
            return self.iterator.next()

        temp = self.peeked_value
        self.peeked_value = None
        self.has_peeked = False
        return temp

    def hasNext(self):
        return self.has_peeked or self.iterator.hasNext()
