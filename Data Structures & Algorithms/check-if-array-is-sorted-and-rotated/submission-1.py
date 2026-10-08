class Solution:
    def check(self, nums: List[int]) -> bool:
        seen = set(nums)    
        for i in range(len(nums)):
            if i not in seen:
                return False
        return True    
