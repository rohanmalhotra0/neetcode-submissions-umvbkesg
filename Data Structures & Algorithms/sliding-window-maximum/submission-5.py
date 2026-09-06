class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        windowSize = k
        k = 2
        j = 1
        i = 0 
        res = []

        if windowSize == len(nums):
            return [max(nums)]
        while k < len(nums):
            maxInWindow = max(nums[i], nums[j], nums[k])
            res.append(maxInWindow)
            i += 1
            j += 1
            k += 1
        return res