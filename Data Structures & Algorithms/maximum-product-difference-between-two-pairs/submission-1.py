class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums1 = nums 
        for num in nums1: 
            num = -num
        heapq.heapify(nums1)
        largest = heapq.heappop(nums1)
        largest2 = heapq.heappop(nums1)
        x = largest * largest2  

        heapq.heapify(nums)
        s = heapq.heappop(nums)
        s2 = heapq.heappop(nums)
        y =s * s2

        return x - y 
        
        