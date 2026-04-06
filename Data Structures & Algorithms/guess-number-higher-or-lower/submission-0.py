# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        mid = n // 2 
        L = 1 
        R = n 
        while L <= R:
            mid =(L + R) // 2
            if 0 == guess(mid):
                return mid
            elif 1 == guess(mid):
                L = mid + 1
            else:
                R = mid - 1