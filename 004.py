# Is linked List Lenght Even

"""
structure of link list node
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
        
"""    
class Solution:
    
    def isEven(self, head):
        # Code here
        count = 0
        while head:
            count += 1
            head = head.next
        if (count % 2 == 0):
            return True
        else:
            return False
