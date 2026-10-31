# 1 to N without loop

class Solution:
    def printTillN(self, n):
    	#code here 
    	if n == 0:
    	    return 0
    	self.printTillN(n - 1)
    	print(n, end = " ")
