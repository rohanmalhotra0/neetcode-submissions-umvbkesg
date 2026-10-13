class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows , cols = len(grid) ,len(grid[0])
        seen = set()
        count = 0 
        q = deque()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        def bfs(r,c):
            q.append((r,c))
            seen.add((r,c))
            while q:
                x, y = q.popleft()
                for dx , dy in directions:
                    nx , ny = x + dx , y + dy
                    if  (0 <= nx < rows 
                        and 0 <= ny < cols 
                        and grid[nx][ny] not in seen  
                        and grid[nx][ny] == '1'):
                        q.append((r,c))
                        seen.add((r,c))
        



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in seen:
                    bfs(r,c)
                    count += 1
        return count
        