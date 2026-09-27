class Solution:
    def myPow(self, x: float, n: int) -> float:
        j = x 
        for i in range(n-1):
            j *= x 
        return j