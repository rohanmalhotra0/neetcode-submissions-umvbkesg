from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = Counter(s1)

        l = 0
        r = len(s1) - 1

        while r < len(s2):
            window = s2[l:r + 1]

            if Counter(window) == target:
                return True

            l += 1
            r += 1

        return False