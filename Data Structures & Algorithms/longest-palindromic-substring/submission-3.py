class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen= 0 
        pair = [-1,-1]
        for i in range(len(s)):
            self.isPal(s, i, i)
            self.isPal(s, i, i+1)
        
        def isPal(self, s, l, r):
            while r < len(s) and l >= 0 and s[r] == s[l]:
                length = r - l + 1
                if maxLen < length:
                    maxLen = length 
                    pair = [l,r+1]
                r += 1
                l -= 1

        return s[pair[0],pair[1]]