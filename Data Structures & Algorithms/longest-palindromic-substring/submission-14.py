class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        pair = [0, 0]

        def isPal(l, r):
            nonlocal maxLen, pair
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    pair = [l, r + 1]
                l -= 1
                r += 1

        for i in range(len(s)):
            isPal(i, i)
            isPal(i, i + 1)
        return s[pair[0]:pair[1]]
        