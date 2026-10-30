# Average of Prefixes

class Solution:
    def prefixAvg(self, arr):
        # code here
        new_arr = []
        n = 1
        total = 0
        for i in range(len(arr)):
            total += arr[i]
            new = total // n
            new_arr.append(new)
            n += 1
        return new_arr
