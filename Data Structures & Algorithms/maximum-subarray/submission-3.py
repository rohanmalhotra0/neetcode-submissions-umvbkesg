class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        
        maxSum = -float('inf')
        for num in nums:
            currSum += num
            currSum = max(currSum, 0)
            maxSum = max(maxSum, currSum)
        return maxSum