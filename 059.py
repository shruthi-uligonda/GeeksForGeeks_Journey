# Arithmetic Number

class Solution:
    def inSequence(self, a: int, b: int, c: int) -> int:
        # code here
        if c == 0:
            return b == a
        if (b - a) >= 0 and (b - a) % c == 0:
            return True
        return False
