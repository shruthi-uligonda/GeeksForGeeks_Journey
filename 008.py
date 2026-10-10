# Length of Circular

''' Linked List Node Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def getLength(self, head):
        # code here
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
            if(temp == head):
                break
        return count
