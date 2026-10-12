class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        memo = {}
        def dfs(i, j):
            if i >= len(triplets):
                return False
            if j >= len(triplets):
                return False
            if (i,j) in memo:
                return memo[(i,j)]
            curSum = []
            curSum.append(max(triplets[i][0], triplets[j][0]))
            curSum.append(max(triplets[i][1], triplets[j][1]))
            curSum.append(max(triplets[i][2], triplets[j][2]))
            if curSum == target:
                return True
            else:
                memo[(i,j)] = dfs(i, j+1) or dfs(i+1, j) or dfs(i+1, j+1)
            return memo[(i,j)]
        return dfs(0,0)