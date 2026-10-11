class Solution:
    def check(self, nums: List[int]) -> bool:
        pivot = -1

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                pivot = i
                break

        if pivot == -1:
            return True

        for i in range(1, pivot):
            if nums[i - 1] > nums[i]:
                return False

        for i in range(pivot + 1, len(nums)):
            if nums[i - 1] > nums[i]:
                return False

        return nums[-1] <= nums[0]