# Check for 4 Sum

class Solution:
    def fourSum(self, arr: list[int], x: int) -> bool:
        """ code here """
        n = len(arr)
        seen = set()
        for i in range(n):
            for j in range(i + 1, n):
                need = x - arr[i] - arr[j]
                if need in seen:
                    return True
            for j in range(i):
                seen.add(arr[i] + arr[j])
        return False
