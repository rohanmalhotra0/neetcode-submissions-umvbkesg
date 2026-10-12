class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = defaultdict(lambda: float('inf'))
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        def dfs(i , j):
            if i == len(word1):
                return len(word2) - j

            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            if word1[i] != word2[j]:
                insert = 1 + dfs(i, j + 1)
                delete = 1 + dfs(i + 1, j)
                replace = 1 + dfs(i + 1, j + 1)
            memo[(i,j)] = min(replace, insert, memo[(i,j)])
            
        return dfs(0,0)
