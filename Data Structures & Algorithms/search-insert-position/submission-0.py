class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
         l , r = 0 , len(nums) -1 
         while l < r:
            m = (l+r) // 2
            if nums[m] > target:
                l = m+1
            if nums[m] < target:
                r = m
            if num[m] == target:
                return m
         return l