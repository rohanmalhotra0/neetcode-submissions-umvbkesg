class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxVal =0 
        for v in count.values():
            if v == 1:
                maxVal = max(maxVal, v)
        
        return maxVal