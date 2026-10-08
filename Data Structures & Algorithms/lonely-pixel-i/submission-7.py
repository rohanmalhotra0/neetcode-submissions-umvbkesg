class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        count = 0
        rows, cols = len(picture) ,len(picture[0])
        checkCol = [False] * cols 
        checkRow = [False] * rows 
        for r in range(rows):
            for c in range(cols):
                if picture[r][c] == 'B':
                    if checkRow[r] or checkCol[c]:
                        continue
                    else:
                        count += 1 
                        checkCol[c] = True
                        checkRow[r] = True
        return count