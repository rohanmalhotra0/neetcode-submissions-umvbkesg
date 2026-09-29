class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sCount = Counter(s)
        tCount = Counter(t)
        for c in t:
            if c in sCount and sCount[c] >= 1:
                sCount[c] -= 1
        return min(sCount) == 0 