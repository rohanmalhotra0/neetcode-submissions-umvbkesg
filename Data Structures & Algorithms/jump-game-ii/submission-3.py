class Solution:
    def jump(self, nums: List[int]) -> int:
        minStep = float('inf')
        memo = {}  # index -> minimum steps used to reach this index

        def dfs(i, steps):
            nonlocal minStep

            if i > len(nums) - 1:
                return

            if i == len(nums) - 1:
                minStep = min(minStep, steps)
                return

            # We've already reached i in fewer/equal steps
            if i in memo and memo[i] <= steps:
                return

            # Best number of steps we've seen for this index
            memo[i] = steps

            for j in range(1, nums[i] + 1):
                dfs(i + j, steps + 1)

        dfs(0, 0)
        return minStep