# Remove Duplicates using Two Pointers

class Solution:
    def removeDuplicates(self, arr):
        # code here 
        left = 0
        n = len(arr)
        for right in range(1, n):
            if arr[left] != arr[right]:
                left += 1
                arr[left] = arr[right]
        return arr[:left + 1]
