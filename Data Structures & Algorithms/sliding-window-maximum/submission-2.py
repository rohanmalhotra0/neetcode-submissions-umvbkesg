class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        final = []
        if len(nums) <= 3:
            for curr in nums:
                curr = max(curr, prevMax)
            final.append(curr)
            return final

        lOut = 0
        rOut = lOut + 3
        prevMax = 0
        curr = 0
        final = []
        while rOut <= len(nums):
            while curr < rOut:
                prevMax = max(prevMax, nums[curr])
                
                curr += 1
            lOut += 1 
            rOut += 1 
            curr = lOut 
            final.append(prevMax)
            prevMax = 0
        return final
