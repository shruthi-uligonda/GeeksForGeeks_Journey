# Printing Linked List

'''class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def printList(self, head):
        # code here
        result = []
        while head:
            result.append(head.data)
            head = head.next
        return result
