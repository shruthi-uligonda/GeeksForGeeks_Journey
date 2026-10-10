# Linked List insertion at Beginning 

"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
"""

class Solution:
    def insertAtFront(self, head, x):
        #code here
        nn = Node(x)
        if head is None:
            nn = Node(x)
            return head
        nn.next = head
        head = nn
        return head
