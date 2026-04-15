class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(len(nums), i+1):
                curr = 0
                curr *= nums[j]  
                res.append(curr)
        return res  
            