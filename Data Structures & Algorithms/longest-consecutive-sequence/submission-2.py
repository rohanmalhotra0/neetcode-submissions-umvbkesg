class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0 

        minNum = min(nums)
        maxNum = max(nums)

        numsFilter = [0] * (maxNum - minNum + 1)

        for num in nums:
            numsFilter[num - minNum] = 1

        for i in range(len(nums)):
            numsFilter[num - minNum] = 1
        longest = 0
        l = 0 
        r = 0  
        for r in range(len(numsFilter)):
            if numsFilter[r] == 1:
                longest = max(longest, r - l + 1)
            else:
                l = r + 1
        return longest 