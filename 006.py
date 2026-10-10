# Linked List End Insertion

'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        data = Node(x)
        if head is None:
            return data
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = data 
        return head
        
    
