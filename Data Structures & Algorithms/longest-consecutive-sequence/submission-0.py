class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0 

        lengthOfFilter = max(nums) + 1 
        numsFilter = [0] * lengthOfFilter

        for i in range(len(nums)):
            numsFilter[nums[i]] = 1 
        longest = 0
        l = 0 
        r = 0  
        for r in range(len(numsFilter)):
            if numsFilter[r] == 1:
                longest = max(longest, r - l + 1)
            else:
                l = r + 1
        return longest 