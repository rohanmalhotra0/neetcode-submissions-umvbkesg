class Solution:
    def jump(self, nums: List[int]) -> int:
        minStep = float('inf')
        def dfs(i, steps):
            nonlocal minStep

            if i > (len(nums) - 1):
                return
            if i == (len(nums) - 1):
                minStep = min(minStep, steps)
                return
            
            for j in range(1, nums[i]+1):
                dfs(i + j, steps + 1)

        dfs(0,0)
        return minStep