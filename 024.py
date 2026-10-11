# Armstrong

class Solution:
    def armstrongNumber (self, n):
        # code here 
        temp = n
        power = 0
        count = len(str(n))
        temp = n
        while temp > 0:
            digit = temp % 10
            power += digit**count
            temp //= 10
        if(power == n):
            return True
        else:
            return False
