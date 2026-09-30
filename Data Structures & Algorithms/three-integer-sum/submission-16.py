from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                if currSum == 0:
                    res.append([nums[i] ,nums[l], nums[r]])
                elif currSum > 0:
                    r += 1
                else:
                    l -= 1 
        return res