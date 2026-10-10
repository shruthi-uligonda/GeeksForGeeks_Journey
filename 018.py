# Frequency In Linked List

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''
class Solution:
    def count(self, head, key):
        temp = head
        count = 0
        while temp:
            if(key == temp.data):
                count += 1
            temp = temp.next
        return count
