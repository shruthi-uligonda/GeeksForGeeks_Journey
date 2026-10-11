# Digits of Factorial

class Solution:
    def digitsInFactorial(self,n):
        # code here
        if n <= 1:
            return 1
        return int(
            n * math.log10(n / math.e)
            + 0.5 * math.log10(2*math.pi*n)
            ) + 1
