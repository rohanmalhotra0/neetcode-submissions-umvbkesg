class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        n, m = len(word), len(abbr)
        while r < len(word):
            if word[i] == abbr[j]:
                i, j = i + 1, j + 1
            if abbr[j] == '0':
                return False
            elif abbr[j].isalpha():
                return False
            else:
                subLen = 0
                while j < m and abbr[j].isdigit():
                    subLen = subLen * 10 + int(abbr[j])
                    j += 1
                i += subLen
        return i == n and j == m