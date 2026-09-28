class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = Counter(s)
        if len(s) != len(t):
            return False
        for l in t:
            if l not in counterS[l] or counterS[l] == 0:
                return False
            countS[l] -= 1
        return max(counterS) == 0 
        
     