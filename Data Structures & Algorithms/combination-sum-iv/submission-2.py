class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dfs(i, amount):
            if amount < 0 or i >= len(nums):
                return 0
            if amount == 0:
                return 1

            if amount in memo:
                return memo[amount]
            
            skip = dfs(i, amount - num)
            take = 0
            for j in range(i, len(nums)):
                if amount - num > 0:
                    take += dfs(j, amount - num)
            memo[amount] = take + skip
            return memo[amount]
        return dfs(0, target)

