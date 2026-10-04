class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countRansom = Counter(ransomNote)
        for ch in magazine:
            if ch in countRansom:
                countRansom[ch] -= 1
        return True if max(countRansom.values()) <= 0 else False

