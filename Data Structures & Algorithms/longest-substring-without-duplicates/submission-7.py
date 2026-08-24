
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLen = 0
        l =0
       
        while l < len(s):
            if s[l] not in seen:
                seen.add(s[l])
            else:
                maxLen = max(maxLen, len(seen))
                seen.clear()
            l += 1    
           
        return maxLen