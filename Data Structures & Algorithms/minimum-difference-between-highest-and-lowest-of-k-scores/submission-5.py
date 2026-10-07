class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        r = k - 1   
        l = 0
        res = nums[r] - nums[l]
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l += 1
            r += 1
        return res