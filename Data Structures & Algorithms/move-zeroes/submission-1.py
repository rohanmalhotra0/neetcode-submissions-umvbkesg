class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = len(nums) - 1 
        for i in range(len(nums)):
            if nums[i] == 0 and nums[r] != 0:
                if r == i: break
                nums[i], nums[r] = nums[r], nums[i]
                r-=1
            
            else:
                while r != '0':
                    r -= 1 
                nums[i], nums[r] = nums[r], nums[i]
        