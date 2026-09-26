class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, currSet = [], []

        self.helper(0, subsets, currSet, nums)
        return subsets

    def helper(self, i, subsets, currSet, nums):
        if i >= len(nums):
            subsets.append(currSet.copy())
            return

        # KEEP nums[i]
        currSet.append(nums[i])
        self.helper(i + 1, subsets, currSet, nums)

        # Backtrack
        currSet.pop()

        # SKIP nums[i] and all its duplicates
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        self.helper(i + 1, subsets, currSet, nums)
