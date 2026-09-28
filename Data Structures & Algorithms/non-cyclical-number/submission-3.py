class Solution:
    def isHappy(self, n: int) -> bool:
        n = list(str(n))
        currSum = 0
        for i in range(len(n)):
            currSum += n[i] ** 2
        return currSum == 1
        