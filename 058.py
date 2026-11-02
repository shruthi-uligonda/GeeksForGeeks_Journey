# Max Sum Subarray of Size K

class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        left = 0
        right = 0
        curr_sum = 0
        max_sum = float("-inf")
        while right < len(arr):
            curr_sum += arr[right]
            if right - left + 1 == k:
                max_sum = max(max_sum, curr_sum)
                curr_sum -= arr[left]
                left += 1
            right += 1
        return max_sum
