class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0 
        maxSum = 0
        for num in nums:
            currSum += num
            currSum = max(currSum, 0)
            maxSum = max(maxSum, currSum)
        return maxSum