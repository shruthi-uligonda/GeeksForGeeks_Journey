# Count 1s in Binary Array

class Solution:
    def countOnes(self, arr):
        #code here
        count = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                count += 1
        return count
