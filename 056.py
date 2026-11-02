# Level Order Traversal

''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def levelOrder(self, root):
        # code here
        if root is None:
            return []
        queue = []
        result = []
        queue.append(root)
        queue.append(None)
        while queue:
            curr = queue.pop(0)
            if curr is None:
                if len(queue) == 0:
                    break
                else:
                    queue.append(None)
            else:
                result.append(curr.data)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                     queue.append(curr.right)
        return result
