class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        stack = []
        if nums[0] <= nums[len(nums) - 1]:

            for i in range(len(nums)):
                while stack and stack[-1] >= nums[i]:
                    stack.pop()
                stack.append(nums[i])

            return stack
        else:
            for i in range(len(nums)):
                while stack and stack[-1] <= nums[i]:
                    stack.pop()
                stack.append(nums[i])

            return stack