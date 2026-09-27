class Solution:
    def myPow(self, x: float, n: int) -> float:
        j = x 
        for i in range(n):
            j *= x 
        return j