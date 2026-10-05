class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        # Base Case: if i >= len(nums) 
        # Memo Check: if memo[i][curr] != -1: return memo[i][curr]
        # Combination Step: return 1 if currSum == Target
        # Case 1: Add To CurrSum 
        # Case 2: Sub from Curr Sum 
        memo = [-1 * len(nums) + 1 for _ in range(len(nums))]
        def backtrack(i, curr):
            if curr == target:
                return 1
            if i >= len(nums):
                return 0 
            if memo[i][curr] != -1: 
                return memo[i][curr]
            
            res = 0
            if target - curr > 0:
                res = backtrack(i+1, curr + nums[i])
                res += backtrack(i+1, curr - nums[i])
            memo[i][curr] = res

            return memo[i][curr]
        return backtrack(0,0)
