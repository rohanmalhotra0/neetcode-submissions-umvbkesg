class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        directions = [(0,-1),(0,1),(1,0), (-1,0)]
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    for dx , dy in directions:
                        nx = r + dx
                        ny = c + dy
                        if 0 <= nx < len(rows) and 0 <= ny < len(cols):
                            grid[nx][ny] = 0 