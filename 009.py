# Middle of Linked List

''' Linked List Node Structure
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    def getMiddle(self, head):
        # code here
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        temp = head
        middle = count // 2
        while middle:
            temp = temp.next
            middle -= 1
        return temp.data
