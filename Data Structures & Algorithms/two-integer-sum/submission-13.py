class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map1:
               return [map1[complement], i]
            else:
               map1[nums[i]] = i
               
