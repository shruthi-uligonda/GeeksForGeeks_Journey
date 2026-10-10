# Insertion in Empty Circular List

""" Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Initially, the next pointer is None.
 """ 
class Solution:
    def insertIntoEmpty(self, last, data):
        # code here
        if last is not None:
            return last

        new_node = Node(data)
        new_node.next = new_node
        return new_node
