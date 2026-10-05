class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums = heapq.heapify(-nums)
        return list(nums)
        