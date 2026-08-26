class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols  = len(grid), len(grid[0])
        visited = set()
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        inf = 2147483647
        
        # More Efficent Use Array for Subproblems already computed
        # take the min of every BFS
        def bfs(i,j):
            q = deque([(i,j)])
            visited.add((i,j))
   
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx , y + dy
                    
                    if (
                    0 <= nx < rows and 
                    0 <= ny < cols and 
                    (nx, ny) not in visited):
                        if grid[nx][ny] == 0:
                            q.append((nx,ny))
                            visited.add((nx,ny))
                        if grid[nx][ny] == inf:
                            
                            visited.add((nx,ny))
                            grid[nx][ny] = grid[x][y] + 1
                            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and (i,j) not in visited:
                    bfs(i,j)
            

