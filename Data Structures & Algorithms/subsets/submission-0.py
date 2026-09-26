class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, currSet = [], []
        helper(0,subsets,currSet)
        return subsets
    def helper(i , subsets, currSet):
        if i >= len(nums):
            subsets.append(currSet.copy)
            return
        # Keep
        helper(i+1, subsets, currSet)
        # Skip 
        while i < len(nums) and nums[i] == nums[i+1]:
            i+=1
        helper(i+1, subsets, currSet)