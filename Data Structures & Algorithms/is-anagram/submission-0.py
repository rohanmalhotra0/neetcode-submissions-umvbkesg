class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s.sort()
        t.sort()
        if s == t:
            return True
        else:
            return False
