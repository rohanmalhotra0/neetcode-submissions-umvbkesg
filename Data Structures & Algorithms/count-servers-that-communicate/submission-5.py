class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        seen = set()
        q = deque()
        rows , cols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)] 
        count = 0
        

        def bfs(r, c):
            nonlocal count
            q.append((r,c))
            seen.add((r,c))
            while q:
                r, c = q.popleft()
               
                for dx, dy in directions:
                    nx,ny = r + dx, dy + c
                    if 0 <= nx < rows and 0 <= ny < cols and (nx,ny) not in seen and grid[nx][ny] == 1:
                        q.append((nx,ny))
                        seen.add((nx,ny))
                        count += 1 
                        
                
                
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in seen:
                    bfs(r,c)
                    count += 1 
                    
        return count