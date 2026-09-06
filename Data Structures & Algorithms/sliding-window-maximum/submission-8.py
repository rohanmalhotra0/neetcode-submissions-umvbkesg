class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        windowSize = k
        res = []
        i=0
      
        for r in range(len(nums)):
            while  (r - i + 1) == windowSize:
                maxInWindow = max(nums[i:r+1])
                i += 1
                res.append(maxInWindow)
            
        return res