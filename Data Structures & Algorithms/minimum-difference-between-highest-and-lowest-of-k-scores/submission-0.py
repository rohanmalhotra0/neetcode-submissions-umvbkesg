class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l += 1
            r += 1
        return res