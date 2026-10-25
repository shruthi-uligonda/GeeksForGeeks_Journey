# Product of Prime factors

class Solution:
    def primeProduct(self, n):
        # code here
        product = 1
        if n == 1:
            return 1
        for i in range(2, n + 1):
            if n % i == 0:
                for j in range(2, int(i ** 0.5) + 1):
                    if i % j == 0:
                        break
                else:
                    product *= i
        return product
