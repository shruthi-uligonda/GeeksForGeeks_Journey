# Count Pairs with Max Diff

class Solution:
    def countPairs(self,arr):
        #code here.
        maximum = max(arr)
        minimum = min(arr)
        
        if maximum == minimum:
            return 0
            
        count_max = arr.count(maximum)
        count_min = arr.count(minimum)
        return count_max * count_min
