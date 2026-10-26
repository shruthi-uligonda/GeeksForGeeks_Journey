# Good Numbers

class Solution:
    def goodNumbers(self, l, r, d):
        # code here
        result = []
        for num in range (l, r + 1):
            s = str(num)
            if str(d) in s:
                continue
            right_sum = 0
            good = True
            
            for i in range(len(s) - 1, -1, -1):
                digit = int(s[i])
                
                if i != len(s) - 1 and digit <= right_sum:
                    good = False
                    break
                
                right_sum += digit
                
            if good:
                result.append(num)
        return result
