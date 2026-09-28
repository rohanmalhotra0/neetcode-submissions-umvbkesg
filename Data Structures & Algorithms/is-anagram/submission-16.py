class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = Counter(s)
        if len(s) != len(t):
            return False
        for l in t:
            if l not in counterS or counterS[l] == 0:
                return False
            counterS[l] -= 1
        print(counterS)
        return max(counterS) == 0 
        
     