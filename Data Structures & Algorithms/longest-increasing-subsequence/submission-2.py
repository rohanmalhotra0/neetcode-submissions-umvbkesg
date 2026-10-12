class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, j):
            if i == len(nums):
                return 0
            if (i, j) in memo:
                return memo[(i,j)]
            
            skip = dfs(i + 1, j) # not include
            memo[(i,j)] = skip 
            if j == -1 or nums[j] < nums[i]:
                take = 1 + dfs(i + 1, j + 1) # include
                memo[(i,j)] = max(take, skip)
            return memo[(i,j)]

        return dfs(0, -1)