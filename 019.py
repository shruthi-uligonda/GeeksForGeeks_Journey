# Sum of Last n Nodes of Linked List

''' Structure for link list Node
    class Node:
        def __init__(self, val):
            self.data = val
            self.next = None
'''

class Solution:
    def sumofNodes(self, head, n):
        # code here
        temp = head
        sum = 0
        count = 0
        while temp:
            count += 1
            temp = temp.next
        value = count - n
        temp = head
        while value :
            temp = temp.next
            value -= 1
        while temp:
            sum += temp.data
            temp = temp.next
        return sum
