class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        count = 0
        rows, cols = len(picture), len(picture[0])
        checkCol = [0] * cols
        checkRow = [0] * rows

        for r in range(rows):
            for c in range(cols):
                if picture[r][c] == 'B':
                    checkCol[c] += 1
                    checkRow[r] += 1

        for r in range(rows):
            for c in range(cols):
                if picture[r][c] == 'B':
                    if checkRow[r] != 1 or checkCol[c] != 1:
                        continue
                    else:
                        count += 1

        return count