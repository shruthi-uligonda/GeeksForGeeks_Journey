# Check InOrder Of BST

class Solution:
    def  doesRepresentBST(self, arr):
        # code here
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                return False
        return True
