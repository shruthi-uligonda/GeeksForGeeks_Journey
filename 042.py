# Count Numbers with Digit 4

class Solution:
    def countNumberswith4(self, n: int) -> int:
        # code here
        count = 0
        for i in range(1, n + 1):
            temp = i
            while temp > 0:
                digit = temp % 10
                if digit == 4:
                    count += 1
                    break
                temp //= 10
        return count
