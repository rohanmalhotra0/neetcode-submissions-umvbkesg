class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        
        maxSum = nums[0]
        for i in range(1, len(nums)):
            currSum += nums[i]
            currSum = max(currSum, 0)
            
            maxSum = max(maxSum, currSum)
        return maxSum