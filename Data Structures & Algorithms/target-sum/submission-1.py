class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        # Base Case: if i >= len(nums) 
        # Memo Check: if memo[i][curr] != -1: return memo[i][curr]
        # Combination Step: return 1 if currSum == Target
        # Case 1: Add To CurrSum 
        # Case 2: Sub from Curr Sum 
    
        memo = {}

        def backtrack(i, curr):

            # Base case: used every number
            if i >= len(nums):
                return 1 if curr == target else 0

            # Memo check
            if (i, curr) in memo:
                return memo[(i, curr)]

            # Case 1: +
            add = backtrack(i + 1, curr + nums[i])

            # Case 2: -
            subtract = backtrack(i + 1, curr - nums[i])

            memo[(i, curr)] = add + subtract

            return memo[(i, curr)]

        return backtrack(0, 0)