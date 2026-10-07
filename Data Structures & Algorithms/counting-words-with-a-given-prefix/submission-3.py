class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        minLen = len(pref)
        count = Counter(pref)
        for word in words:
            for i in range (len(pref)):
                if word[i] != pref[i]:
                    inc = 0 
                    break
            res += inc
