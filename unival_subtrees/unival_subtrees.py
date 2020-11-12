"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def set_child(self, direction, value):
        if direction == "left":
            self.left = Node(value)
        elif direction == "right":
            self.right = Node(value)


tree_root = Node(0)
tree_root.set_child("left", 1)
tree_root.set_child("right", 0)
tree_root.right.set_child("left", 1)
tree_root.right.set_child("right", 0)
tree_root.right.left.set_child("left", 1)
tree_root.right.left.set_child("right", 1)


count = 0
"""
def counter(function):
    def wrapper():
        count = 0
        return function
"""

tree_no = 0
def count_unival(tree):
    global tree_no
    if tree is None:
        return True

    if (tree.left is None or tree.left.value == tree.value) and (tree.right is None or tree.right.value == tree.value):
        if count_unival(tree.left) and count_unival(tree.right):
            tree_no += 1
            print(tree_no)
            return True
    else:
        count_unival(tree.left)
        count_unival(tree.right)
        print(tree_no)
        return False



count_unival(tree_root)
