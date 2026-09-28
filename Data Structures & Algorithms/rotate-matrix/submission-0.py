class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for r in range(rows):
            for c in range(cols):
                matrix[r][c] = matrix[c][r]
        print(matrix)