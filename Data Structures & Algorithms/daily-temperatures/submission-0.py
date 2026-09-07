class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nums = temperatures
        stack = []
        res = [0] * len(temperatures)

        for i, val in enumerate(nums):
            # Pop elements that current value resolves
            while stack and nums[stack[-1]] < val:
                j = stack.pop()
                if nums[i] > nums[j]:
                    res[j] = i-j
               
            stack.append(i)
        return res