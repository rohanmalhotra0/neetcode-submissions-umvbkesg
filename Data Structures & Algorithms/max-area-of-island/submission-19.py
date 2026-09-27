class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        
        def dfs(r,c):
            if (min(r,c) < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] != 1):
                return 0 
            visited.add(r,c)
            
            curr = 1
            curr += dfs(r + 1, c)
            curr += dfs(r - 1, c)
            curr += dfs(r, c + 1)
            curr += dfs(r, c - 1)
            return curr

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    visited.add(r,c)
                    curr = dfs(r,c)
                    maxArea = max(curr, maxArea)
        return maxArea

