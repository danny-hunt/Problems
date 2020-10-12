"""
Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   21
  /  \
 5    30
     /  \
   22    35
     \
      27
        \
         28

You can assume each node has a parent pointer.
"""

# Given a node we need to check the smallest node in its right subtree
# If that doesn't exist then go through ancestors - the first ancestor that is a right-parent of the path is the IS
# Otherwise one doesn't exist


def inorder_successor(node):
    current_node = node
    if node.right_child:
        current_node = node.right_child
        while current_node.left_child:
            current_node = current_node.left_child
        return current_node.value
    else:
        while current_node.parent:
            if current_node.value < current_node.parent.value:
                return current_node.parent.value
            current_node = node.parent
        return node.value
