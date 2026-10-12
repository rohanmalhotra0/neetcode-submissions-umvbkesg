class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        rows , cols = len(grid), len(grid[0])

        def dfs(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return float('inf')
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]
            if (r, c) in memo:
                return memo[(r,c)]
            memo[(r,c)] = grid[r][c] + min(dfs(r+1, c), dfs(r,c+1))
            return memo[(r,c)]


        return dfs(0,0)