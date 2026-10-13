# Magic Number

class Solution:
    def nthMagicNo(self, n: int) -> int:
        # code here
        ans = 0
        power = 5 
        while n > 0:
            if n % 2 == 1:
                ans += power
            power *= 5
            n //= 2
        return ans
