class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)

        index = 0
        for val in range(min(nums), max(nums) + 1):
            while count[val] > 0:
                nums[index] = val
                index += 1
                count[val] -= 1

        return nums