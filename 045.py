# Mean and Median

class Solution:
    def median(self, arr):
        # code here
        arr.sort()
        length = len(arr)
        value = length // 2
        if length % 2 != 0:
            return arr[value]
        else:
            return (arr[value - 1] + arr[value]) // 2
    def mean(self, arr):
        # code here
        length = len(arr)
        sum_of_arr = sum(arr)
        return int(sum_of_arr / length)
