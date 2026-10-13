# Delete Middle from Linked List

""" Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def deleteMid(self, head):
        if head is None:
            return None
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        if n == 1:
            return None
        temp = head
        n = n // 2
        while n > 1:
            temp = temp.next
            n -= 1
        temp.next = temp.next.next
        return head
        
        
       
