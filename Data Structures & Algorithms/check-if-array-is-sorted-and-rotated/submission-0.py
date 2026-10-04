class Solution:
    def check(self, nums: List[int]) -> bool:
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev > nums[i]:
                return False
            prev = nums[i]
        return True
