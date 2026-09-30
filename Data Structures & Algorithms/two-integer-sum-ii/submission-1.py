class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l , r = 0 , len(numbers) - 1
        while l < r: 
            count = nums[l] + nums[r]
            if count == target:
                return [l+1, r+1]
            elif count > target:
                r -= 1 
            else:
                l += 1 
        return []
              