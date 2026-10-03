class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxVal = float('-inf')
        for k, v in count.items():
            if v == 1:
                maxVal = max(maxVal, k)
        
        return maxVal