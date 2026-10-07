class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        r = 0 
        maxCount = 0
        count = 0
        flag = 0 
        while r < len(nums):
            count = 0 
            l = r
            while (r < len(nums) and nums[r] == 1) or flag == 0:
                if r < len(nums) and nums[r] != 1:
                    flag += 1 
                count += 1
                r += 1
            maxCount = max(count, maxCount)
            flag = 0
            r = l + 1 
        return count
            