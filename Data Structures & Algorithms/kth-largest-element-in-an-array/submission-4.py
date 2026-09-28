class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """for num in nums:
            num = -num"""
        heapq.nlargest(k, nums)[-1]