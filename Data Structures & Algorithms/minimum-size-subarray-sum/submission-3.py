class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r  = 0 , 1 
        minLen = float('inf') 
        currSum = nums[0]
        while r < len(nums):
            currSum += nums[r]
            while currSum >= target:
                minLen = min(minLen, r - l)
                currSum -= nums[l]
                l += 1 
            r+=1
        return minLen if minLen != float('inf') else 0