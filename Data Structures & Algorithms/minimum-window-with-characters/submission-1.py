class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t or not s:
            return ""

        countT = [0] * 100

        minStr = "Q" * 10000
        for ch in t:
            countT[ord(ch) - 65] += 1
        
        l = 0
        countTDupe = countT.copy()
        
        for r in range(len(s)):
            countT = countTDupe.copy()

            if countT[ord(s[r]) - 65] >= 1 and countT:
                l = r
                #countT[ord(s[r]) - 65] -= 1
                
                while r < len(s):
                    
                    if countT[ord(s[r])- 65] >= 1 and countT:
                        countT[ord(s[r]) - 65] -= 1
                        
                        if  max(countT) == 0:
                            if len(minStr) > len(s[l:r+1]):
                                minStr = s[l:r+1]
                                break    
                    r+=1
        
        if minStr != ("Q"*10000):
            return minStr
        return ""