class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[0] <= nums[-1]:
            # should be non-decreasing
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    return False
        else:
            # should be non-increasing
            for i in range(1, len(nums)):
                if nums[i] > nums[i - 1]:
                    return False

        return True