class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visit = set()
        maxArea = 0 
        rows , cols = len(grid) , len(grid[0])
        directions = [(-1,0), (1, 0), (0,-1), (0,1)]
        def dfs(r,c):
            if (
                r < 0 or
                c < 0 or
                c >= cols or
                r >= rows or 
                grid[r][c] == 0 or
                (r,c) in visit
            ):
                return 0
            visit.add((r,c))
            curr = 1
            for dx , dy in directions:
                curr += dfs(r + dr, c + dc)
            return curr
        for r in range(rows):
            for c in range(cols):
                curr = 0
                if grid[r][c] == 1 and (r,c) not in visit:
                    curr = dfs(r,c)
                    maxArea = (curr, maxArea)
        return maxArea


