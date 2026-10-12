class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        memo = {}
        
        maxCount = float('inf')
        def dfs(r , c):
            
            if r < 0 or c < 0 or r >= rows or c >= cols or obstacleGrid[r][c] == 1:
                return 0
               
            if (r,c) in memo:
                return memo[(r,c)]

            if r == rows - 1 and c ==cols - 1:
                return 1
    
            right = dfs(r+1, c)
            down = dfs(r, c+1)
            memo[(r,c)] = right + down
            return memo[(r,c)]
        return dfs(0,0)
