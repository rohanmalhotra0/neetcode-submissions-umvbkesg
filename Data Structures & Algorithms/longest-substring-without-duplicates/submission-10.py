
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLen = 0
        l = 0
        r = 0

        while r < len(s):

            # duplicate? shrink from the LEFT
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            # now s[r] is safe to add
            seen.add(s[r])

            maxLen = max(maxLen, r - l + 1)

            r += 1

        return maxLen