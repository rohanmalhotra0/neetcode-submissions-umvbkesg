class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        curr = nums[0]
        for i in range (1, len(nums)):
            if curr + nums[i] == target:
                return [i - 1, i]
        
