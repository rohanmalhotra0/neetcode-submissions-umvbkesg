class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        maxArea = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and  grid[r][c]== 1:
                    q = deque()
                    q.append((r, c))
                    visited.add((r, c))

                cur = 0
                while q:
                    
                    x, y = q.pop()
                    cur += 1
                    
                    for dx , dy in directions:
                        nx , ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and (nx,ny) not in visited:
                            if grid[nx][ny] == 1:
                                visited.add((r,c))
                                q.append((r,c))
                                
                    maxArea = max(maxArea, cur)
        return maxArea

"""

        def dfs(r,c):
            if (min(r,c) < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] != 1):
                return 0 
                
            visited.add((r,c))
            
            curr = 1
            curr += dfs(r + 1, c)
            curr += dfs(r - 1, c)
            curr += dfs(r, c + 1)
            curr += dfs(r, c - 1)
            return curr

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                   
                    curr = dfs(r,c)
                    maxArea = max(curr, maxArea)
        return maxArea

"""