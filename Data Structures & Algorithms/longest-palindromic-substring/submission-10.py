class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.maxLen = 0
        self.pair = [0, 0]
        for i in range(len(s)):
            self.isPal(s, i, i)
            self.isPal(s, i, i + 1)
        l, r = self.pair
        return s[l:r]

    def isPal(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            length = r - l + 1
            if length > self.maxLen:
                self.maxLen = length
                self.pair = [l, r + 1]
            l -= 1
            r += 1