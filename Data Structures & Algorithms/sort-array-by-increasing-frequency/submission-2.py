class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        for num in nums:
            num = -num
        maxFreq = heapq.heapify(nums)
        return list(maxFreq)
        