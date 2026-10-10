# Check if Circular Linked List

#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


class Solution:
    def isCircular(self, head):
        # code here
        if head is None:
            return True
        temp = head.next
        while temp and temp != head:
            temp = temp.next
        if(temp == head):
            return True
        return False
