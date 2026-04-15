class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) -1 

        while l <= r:
            m = (l + r) // 2
            if nums[l] > nums[r] and nums[m] != target:
                l = m + 1
            elif nums[r] > nums[l] and nums[m] != target:
                r = m - 1
            elif nums[m] == target:
                return m
            else:
                return -1 
            