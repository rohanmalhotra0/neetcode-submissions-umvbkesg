class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        r = 0
        maxCount = 0
        curr = 0
        while r < len(nums):
            curr = 0
            while r < len(nums) and nums[r] == 1:
                curr += 1
                r += 1
            r += 1 
            maxCount = max(curr, maxCount)
        return maxCount
