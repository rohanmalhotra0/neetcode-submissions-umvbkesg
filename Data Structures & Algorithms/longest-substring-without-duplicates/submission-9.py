
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLen = 0
        l = 0
        r = 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                maxLen = max(maxLen, len(seen))
                r += 1
            else:
                seen.remove(s[l])
                l += 1

        return maxLen