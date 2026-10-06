class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        index = 0
        for val in range(min(nums), max(nums) + 1):
            while count[val] > 0:
                nums[index] = val
                index += 1
                count[val] -= 1

        return nums