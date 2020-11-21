"""
Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint
that the key in the left child must be less than or equal to the root and the key in the right
child must be greater than or equal to the root.
"""

def valid_section(tree):
    if tree is None:
        return True

    going_to_be = True
    if tree.left is not None:
        if tree.left.value > tree.value:
            going_to_be = False
    if tree.right is not None:
        if tree.right.value < tree.value:
            going_to_be = False
    return going_to_be


def valid_bst(tree):
    if valid_section(tree):
        return valid_bst(tree.left) and valid_bst(tree.right)
