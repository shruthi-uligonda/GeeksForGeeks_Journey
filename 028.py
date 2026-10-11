# Strong Numbers

class Solution:
    def isStrong(self, n):
        # code here
        if n < 0:
            return False
        fac = 1
        sum = 0
        temp = n
        while n > 0:
            digit = n % 10
            fac = 1
            for i in range(1, digit + 1):
                fac *= i
            sum += fac
            n //= 10
        return sum == temp
