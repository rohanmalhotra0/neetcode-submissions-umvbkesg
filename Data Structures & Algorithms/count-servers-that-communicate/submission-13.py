class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        seen = set()
        q = deque()
        rows , cols = len(grid), len(grid[0])
        directions = [(1,0),(0,1)] 
        
        size = 0 

        def bfs(r, c):
            count = 0
            q.append((r,c))
            seen.add((r,c))
            while q:
                r, c = q.popleft()
                count += 1 
                for nc in range(cols):
                    if grid[r][nc] == 1 and (r, nc) not in seen:
                        seen.add((r, nc))
                        q.append((r, nc))

                # Check entire column
                for nr in range(rows):
                    if grid[nr][c] == 1 and (nr, c) not in seen:
                        seen.add((nr, c))
                        q.append((nr, c))
            return count
                        
                        
                
                
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in seen:
                    count = bfs(r,c)
                    if count > 1:
                        size += count
                        
        return size
