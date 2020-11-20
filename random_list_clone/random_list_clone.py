"""
Given the head to a singly linked list,
where each node also has a “random” pointer that points to anywhere in the linked list,
deep clone the list.
"""



class Node:
    def __init__(self, value, next=None, random=None):
        self.value = value
        self.next = next
        self.random = random

def deepcopy(head):
    old_head = head
    new_node = Node(old_head.value)
    new_next = Node(old_head.value)
    new_node.next = new_next

