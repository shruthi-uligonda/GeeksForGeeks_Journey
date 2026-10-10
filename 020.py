# Insert at Middle of Linked List

'''
structure of a linked list node 
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def insertInMiddle(self, head, x):
        #code here
        nn = Node(x)
        count = value = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        value = (count - 1) // 2
        temp = head
        if head is None:
            return nn
        while value:
            temp = temp.next
            value -= 1
        nn.next = temp.next
        temp.next = nn
        return head
