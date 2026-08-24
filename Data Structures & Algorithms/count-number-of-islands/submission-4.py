from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,j):
            q = collections.deque()
            q.append((i,j))
            seen.add((i,j))
            while q:
                x,y = q.popleft()
                for dx , dy in directions:
                    nx , ny = dx + x, dy + y
                    if 0 <= nx < rows and  0 <= ny < cols and grid[nx][ny] == '1' and (nx, ny) not in seen:
                        q.appened(nx,ny)
                        seen.add((nx,ny))

        if not grid[0] or not grid:
           return 0
        rows , cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        seen = set()
        island = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in seen:
                    bfs(i,j)
                    island += 1
        return island
