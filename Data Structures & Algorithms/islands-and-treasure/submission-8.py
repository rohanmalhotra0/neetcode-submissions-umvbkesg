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
            count = 1
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx , y + dy
                    if (
                    0 <= nx < rows and 
                    0 <= ny < cols and 
                    grid[nx][ny] == inf and 
                    (nx, ny) not in visited):
                        if grid[nx][ny] == inf:
                            q.append((nx,ny))
                            visited.add((nx,ny))
                            grid[nx][ny] = min(count, grid[nx][ny])
                    count += 1


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and (i,j) not in visited:
                    bfs(i,j)
            

