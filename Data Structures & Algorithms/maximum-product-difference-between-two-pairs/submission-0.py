class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums1 = nums 
        for num in nums1: 
            num = -num
        heapq.heapify(nums1)
        largest = heapq.heappop()
        largest2 = heapq.heappop()
        x = largest * largest2  

        heapq.heapify(nums)
        s = heapq.heappop()
        s2 = heapq.heappop()
        y =s * s2

        return x - y 
        
        