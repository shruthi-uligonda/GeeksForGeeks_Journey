# Deletion at the End of the Linked List

''' Linked List Node Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def removeLastNode(self, head):
        # code here
        temp = head
        prev = None
        if head.next is None:
            head = None
            return head
        while temp.next != None:
            prev = temp
            temp = temp.next
        prev.next = None
        return head
            
        
