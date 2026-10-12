# Move all Negative to the End

class Solution:
    def segregateElements(self, arr):
        # code here
        temp = []
        for i in range(len(arr)):
            if arr[i] >= 0:
                temp.append(arr[i])
        for i in range(len(arr)):
            if(arr[i] < 0):
                temp.append(arr[i])
        for i in range(len(arr)):
            arr[i] = temp[i]
        return arr
                
