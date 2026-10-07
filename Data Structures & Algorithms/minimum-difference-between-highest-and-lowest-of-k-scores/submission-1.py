class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        r = len(nums) - 1  
        l = 0
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l += 1
            r += 1
        return res