"""
Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
"""


def find_deepest(root):
    search_set = [root]
    while search_set != []:
        for node in search_set:
            if hasattr(node, "left"):
                search_set.append(node.left)
            if hasattr(node, "right"):
                search_set.append(node.right)
            if len(search_set) == 1:
                return search_set[0]
            else:
                search_set.remove(node)


class Node:
    def __init__(self, value, parent=None, direction=None):
        self.value = value
        self.parent = parent
        if direction == "left":
            self.parent.left = self
        elif direction == "right":
            self.parent.right = self


a = Node("a")
b = Node("b", a, "left")
d = Node("d", b, "left")
c = Node("c", a, "right")

print(find_deepest(a).value)
