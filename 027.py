# Divisibility by 8

class Solution:
    def isDivBy8(self, s):
        # code here
        n = 0
        for i in s:
            n = (n * 10 + int(i)) % 8
        if n == 0:
            return True
        else:
            return False
