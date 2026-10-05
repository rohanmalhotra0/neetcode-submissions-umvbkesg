class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        for num in nums:
            num = -num
        heapq.heapify(nums)
        return list(nums)
        