class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = len(nums) - 1 
        while l < r:
            if nums[l] == nums[r] and k >= abs(r-l):
                return True
            r -= 1 
            l += 1

        return False 
