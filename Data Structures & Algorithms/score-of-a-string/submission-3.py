class Solution:
    def scoreOfString(self, s: str) -> int:
        curr = 0
        total = 0
        for i in range(1, len(s)):
            curr = abs(ord(s[i]) - ord(s[i-1]))
            total += curr

        return total