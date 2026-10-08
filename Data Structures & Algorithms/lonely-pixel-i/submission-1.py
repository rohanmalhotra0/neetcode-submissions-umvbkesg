class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        count = 0
        rows, cols = len(picture) ,len(picture[0])
        checkCol = [False] * cols
        checkRow = [False] * rows
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'B':
                    if checkRow[c] or checkRow[r]:
                        continue
                    else:
                        count += 1 
                        checkRow[c] = True
                        checkRow[r] = True
        return count