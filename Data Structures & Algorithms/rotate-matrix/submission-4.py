class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        matrix.reverse()
        for r in range(rows):
            for c in range(cols):
                matrix[r][c] = matrix[c][r]
        