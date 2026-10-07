class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        r = 0 
        maxCount = 0
        count = 0
        while r < len(nums):
            count = 0 
            while r < len(nums) and nums[r] == 1:
                count += 1
                r += 1
            maxCount = max(count, maxCount)
            r += 1
        return count
            