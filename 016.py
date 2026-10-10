# Remove Duplicates in Sorted Linked List

''' Structure of linked list Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

def removeDuplicates(head):
    # code here
    temp = head
    while temp and temp.next:
        if(temp.data == temp.next.data):
            temp.next = temp.next.next
        else:
            temp = temp.next
    return head
