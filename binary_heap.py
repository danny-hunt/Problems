from random import randint
from __future__ import annotations
from typing import List


class BinaryHeap:

    def __init__(self, value):
        self.value = value
        self.children = [None, None]

    def __str__(self):
        return_string = ""
        return_string += str(self.value)
        for child in self.children:
            return_string += str(child)
        return return_string

    @staticmethod
    def __add_node(new_value, heap, parent=None):
        if new_value > heap.value:
            new_node = BinaryHeap(new_value)
            new_node.children[0] = heap
            if parent is not None:
                parent.children[parent.children.index(heap)] = new_node
            return new_node
        else:
            if None in heap.children:
                heap.children[heap.children.index(None)] = BinaryHeap(new_value)
                return heap
            else:
                to_add = heap.children[randint(0, 1)]
                return to_add.__add_node(new_value, to_add, heap)

    def add(self, new_value):
        return self.__add_node(new_value, self)

    def sort(self: BinaryHeap, reverse_list: list=[]) -> List[int]:
        # to be implemented
        pass
    






x = BinaryHeap(5)
x.add(3)
x.add(4)
x.add(2)
x.add(1)
x.add(2)
print(x)