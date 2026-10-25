# Binary Modulo

class Solution:
    def modulo(self, s, m):
        # code here
        value = 0
        for i in range(len(s)):
            rem = int(s[i])
            value = (value * 2 + rem) % m
        return value
