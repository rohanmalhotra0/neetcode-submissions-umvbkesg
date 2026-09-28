class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        zeroRows = set()
        zeroCols = set()

        # Find ORIGINAL zeros
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeroRows.add(r)
                    zeroCols.add(c)

        # Zero cells whose row OR column had a zero
        for r in range(rows):
            for c in range(cols):
                if r in zeroRows or c in zeroCols:
                    matrix[r][c] = 0