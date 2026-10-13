# Smallest Subarray Sum Greater than X

class Solution:
    def smallestSubWithSum(self, x, arr):
        # code here 
        n = len(arr)
        left = 0
        sum = 0
        mini = n + 1
        for right in range(n):
            sum += arr[right]
            while sum > x:
                length = right - left + 1
                if length < mini:
                    mini = length
                sum -= arr[left]
                left += 1
        if mini == n + 1:
            return 0
        else:
            return mini
