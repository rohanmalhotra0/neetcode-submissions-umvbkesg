from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        countS1 = Counter(s1)
        for i in range(len(s2) - len(s1) + 1):
            if s2[i] in countS1:
                countS2 = Counter(s2[i: i + len(s1)])
                if countS2 == countS1: return True
        return False
                