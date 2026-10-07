class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        nums1 = [-num for num in nums]
  
        # heapq.heapify(nums1)
        largest = heapq.heappop(nums1)
        largest2 = heapq.heappop(nums1)
        x = -largest * -largest2  
  
        #heapq.heapify(nums)
        s = heapq.heappop(nums)
        s2 = heapq.heappop(nums)
        y = s * s2

        return x - y 
        
        