"""Implement a PrefixMapSum class with the following methods:

insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.
For example, you should be able to run the following code:

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
"""


class Node:
    def __init__(self, letter, value=0):
        self.letter = letter
        self.children = {}
        self.value = value


def iterate_values(node_list):
    counter = 0
    for node in node_list:
        counter += node.value
        counter += iterate_values(node.children.values())
    return counter


class PrefixMapSum:

    def __init__(self):
        self.children = {}

    def insert(self, key, value):
        current_object = self
        for letter in key:
            if letter not in current_object.children:
                current_object.children[letter] = Node(letter)
            current_object = current_object.children[letter]
        current_object.value = value

    def sum(self, prefix):
        current_object = self
        value_count = 0
        for letter in prefix:
            if letter in current_object.children:
                current_object = current_object.children[letter]
            else:
                return 0
        value_count += current_object.value
        value_count += iterate_values(current_object.children.values())
        return value_count


mapsum = PrefixMapSum()

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5



