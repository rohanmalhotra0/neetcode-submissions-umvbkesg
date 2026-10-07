class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxLen = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            while len(count) > k:
                count[s[l]] -= 1

                if count[s[l]] == 0:
                    del count[s[l]]

                l += 1

            maxLen = max(maxLen, r - l + 1)

        return maxLen