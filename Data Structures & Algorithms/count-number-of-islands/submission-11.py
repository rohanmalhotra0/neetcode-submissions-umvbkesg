from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visit = set()
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or 
                (r,c) in visit or
                grid[r][c] == "0" 
            ):
                return

            visit.add((r,c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and grid[r][c] not in visit:
                    dfs(r, c)
                    islands += 1

        return islands
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        def bfs(i,j):
            q = collections.deque()
            q.append((i,j))
            seen.add((i,j))
            while q:
                x,y = q.popleft()
                for dx , dy in directions:
                    nx , ny = dx + x, dy + y
                    if 0 <= nx < rows and  0 <= ny < cols and grid[nx][ny] == '1' and (nx, ny) not in seen:
                        q.append((nx,ny))
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
        ''' 