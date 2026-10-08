class Solution:
    def minOperations(self, s: str) -> int:
        ones = s.count('1')
        zeros = s.count('0')
        total = (len(s) - max(ones, zeros)) // 2
        return total