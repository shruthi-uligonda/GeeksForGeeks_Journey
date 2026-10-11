# Sum of Squares of First N Natural Numbers

class Solution:
    # Function to calculate the sum of squares of first 'number' natural numbers
    def sumOfSquares(self, number):
        # code here
        squares = 0
        for i in range(1, number + 1):
            squares += i**2
        return squares
