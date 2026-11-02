# Nth of GP from First Two

class Solution:
    def termOfGP(self, a, b, n):
        # code here
        r = b /a
        return int(a * (r**(n - 1)))
