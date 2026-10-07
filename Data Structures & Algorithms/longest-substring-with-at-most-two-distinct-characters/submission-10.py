class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        seen = set()
        r = 0 
        maxLen = 0
        l = 0 
        while r < len(s):
            seen.add(s[r])
            while len(seen) > 2:
                if s[l] in seen: 
                    seen.remove(s[l])
                l += 1
            maxLen = max(maxLen, r - l+ 1)
            r += 1
        print(s[l : r])
        return maxLen