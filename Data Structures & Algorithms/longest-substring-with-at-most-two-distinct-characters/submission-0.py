class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        sameCh = 0 
        maxLen = 0 
        seen = set()
        l = 0 
        for r in range(len(s)):
            if s[r] in seen:
                sameCh += 1
            while sameCh > 2:
                if s[l] == sameCh:
                    sameCh -= 1
                seen.remove(s[l])
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen
