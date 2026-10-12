class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        count = 0
        if len(word1) > len(word2):
            countW1 = Counter(word1)
            countW2 = Counter(word2)
        else:
            countW1 = Counter(word2)
            countW2 = Counter(word1)
        for c, n in countW1.items():
            if c not in countW2:
                count += n
            if n > countW2[c]:
                count += (n - countW2[c])
        return count
