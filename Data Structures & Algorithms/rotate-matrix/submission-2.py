class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                matrix[r][c] = matrix[c][r]
        for r in range(rows-1,0,-1):
            for c in range(cols-1,0,-1):
                matrix[r][c] = matrix[c][r]