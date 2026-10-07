class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0 
        currLen = 0
        seen= set() 

        l = 0
        for r in range(1, len(s)):
            seen.add(s[r])
            while s[l] == s[r]:
                l+=1
                seen.remove(s[l])
            maxLen = max(maxLen, len(s[l:r+1]))
        return maxLen
