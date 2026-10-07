class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 1 
        currLen = 0
        seen= set() 

        l = 0
        for r in range(1, len(s)):
           
            while s[r] in seen:
                l+=1
                seen.remove(s[l])
            seen.add(s[r]) 
            maxLen = max(maxLen, len(s[l:r+1]))
        return maxLen
