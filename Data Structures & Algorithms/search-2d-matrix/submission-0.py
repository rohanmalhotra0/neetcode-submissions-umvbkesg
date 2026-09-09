class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l , r = 0, len(matrix)
        
        for n in range(len(matrix)):
            l , r = 0, len(matrix)
            while l <= r:
                m = (l + r) // 2
                if matrix[n][m] < target:
                    l = m + 1
                elif matrix[n][m] > target:
                    r = m - 1
                else:
                    return True
        return False