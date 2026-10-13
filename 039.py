# Maximum Subarray Sum Limited by X

class Solution:
    def maxSum(self, arr, x):
        # code here
        n = len(arr)
        left = 0
        sum = 0
        maxi = 0
        for right in range(n):
            sum += arr[right]
            while sum > x:
                sum -= arr[left]
                left += 1
            if sum > maxi:
                maxi = sum
        return maxi
