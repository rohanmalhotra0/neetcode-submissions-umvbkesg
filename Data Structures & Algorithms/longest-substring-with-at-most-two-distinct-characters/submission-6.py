class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        seen = set()

        maxLen = 0
        l = 0 
        for r in range(0, len(s)):
            seen.add(s[r])
            while len(seen) > 2:
                if s[l] in seen: 
                    seen.remove(s[l])
                l += 1
            r += 1 
        
            maxLen = max(maxLen, r - l)
        print(s[l : r])
        return maxLen