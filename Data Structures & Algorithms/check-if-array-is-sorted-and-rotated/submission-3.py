class Solution:
    def check(self, nums: List[int]) -> bool:
        seen = set(nums)    
        for i in range(len(nums) - 1):
            if i not in seen:
                return False
        return True    
