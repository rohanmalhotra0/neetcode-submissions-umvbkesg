class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        empty = 0
        fresh = 1
        rotting = 2
        rows , cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0),(0,-1),(0,1)]
        visited = set()
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == rotting:
                    q.append((i,j))
                    visited.add((i,j))
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx , ny = x + dx, y + dy
                if ( 
                    0 <= nx < rows and
                    0 <= ny < cols and
                    grid[nx][ny] == fresh and
                    (nx,ny) not in visited
                ):
                    q.append((nx,ny))
                    visited.add((nx,ny))
                    grid[nx][ny] = grid[x][y] + 1
        maxNum = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == fresh:
                    return -1
                else:
                    maxNum = max(maxNum,grid[i][j])
        return max(0, maxNum - 2) 