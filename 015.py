# Check if Linked List is Sorted

''' Structure of linked list Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def isSorted(self, head):
        # code here
        temp = head
        increasing = True
        decreasing = True
        while temp.next:
            if temp.data > temp.next.data:
                increasing = False
            if temp.data < temp.next.data:
                decreasing = False
            temp = temp.next
        return increasing or decreasing
                
