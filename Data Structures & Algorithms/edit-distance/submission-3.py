class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = defaultdict(int)
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        def dfs(i , j):
            if i >= len(word1) or j >= len(word2):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if word1[i] == word2[j]:
                memo[(i,j)] = 0 + dfs(i+1, j+1) 
                keep = memo[(i,j)]
            replace = 1 + dfs(i+1, j)
            insert = 1 + dfs(i, j+1)
            delete = 1 + dfs(i-1, j)
            memo[(i,j)] = min(replace, insert, keep)
            
        return dfs(0,0)
