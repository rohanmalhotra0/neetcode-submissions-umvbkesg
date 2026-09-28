class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        for word in words:
            if word[:len(pref)] == pref:
                count += 1
        return count