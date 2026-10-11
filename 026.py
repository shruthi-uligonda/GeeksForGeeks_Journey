# Reverse Digits

class Solution:
	def reverseDigits(self, n):
		# Code here
		temp = n
		rev = 0
		while temp > 0:
		    digit = temp % 10
		    rev = rev * 10 + digit
		    temp //= 10
		return rev
