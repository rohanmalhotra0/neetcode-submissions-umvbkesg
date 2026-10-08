class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        dirs = [(0,1),(1,0), (0,-1),(-1,0)]
        seen = set()
        q = deque()
        inf = 2147483647
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            r , c = q.popleft()
            seen.add((r,c))
            for dx, dy in dirs:
                nx, ny = dx + r, dy + c
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] \
                 not in seen and grid[nx][ny] != -1:
                    grid[nx][ny] = grid[r][c] + 1
                    q.append((nx, ny))
                    seen.add((nx,ny))

                

                    
