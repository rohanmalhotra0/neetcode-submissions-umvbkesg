class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 
        while k < len(nums):
            nums[i], nums[k] = nums[k] , nums[i]
            k += 1
            i += 1  