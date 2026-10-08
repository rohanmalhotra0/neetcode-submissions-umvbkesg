class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        count = 0
        rows, cols = len(picture) ,len(picture[0])
        checkCol = [False * cols + 1] 
        checkRow = [False * rows + 1] 
        for r in range(rows):
            for c in range(cols):
                if picture[r][c] == 'B':
                    if checkRow[c] or checkRow[r]:
                        continue
                    else:
                        count += 1 
                        checkRow[c] = True
                        checkRow[r] = True
        return count