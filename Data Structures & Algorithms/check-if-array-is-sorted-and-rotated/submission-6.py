class Solution:
    def check(self, nums: List[int]) -> bool:
        # Case one sorted ret true
        pivot = -1
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                pivot = i
                break 
        if pivot == -1:
            return True
        for i in range(0, pivot):
            if nums[i - 1] > nums[i]:
                return False
        for i in range(pivot, len(nums)):
            if nums[i - 1] < nums[i]:
                return False
        return True