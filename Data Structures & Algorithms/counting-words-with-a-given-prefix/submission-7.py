class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        res = 0
 
        for word in words:
            if len(word) < len(pref):
                continue
            inc = 1
            for i in range (len(pref)):
                if word[i] != pref[i]:
                    inc = 0 
                    break
            res += inc
        return res