class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        
        maxSum = -float('inf')
        for i in range(1, len(nums)):
            if curSum < 0:
                curSum = 0
            maxSum = max(maxSum, currSum)
        return maxSum