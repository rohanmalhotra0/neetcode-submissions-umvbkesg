class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i) # Odd Length
            res += self.countPali(s, i, i + 1) # Even Length
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]: 
            # start from i and work out from the middle
            res += 1
            l -= 1
            r += 1
        return res