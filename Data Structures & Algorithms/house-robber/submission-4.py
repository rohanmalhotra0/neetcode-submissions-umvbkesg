class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        maxProfit = 0
        def dfs(i, total):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(dfs(i+1, total), dfs(i+2, total + nums[i]))
            
            return memo[i]
        


        return dfs(0,0)
            

            