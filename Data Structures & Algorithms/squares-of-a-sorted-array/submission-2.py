class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # lets find the pivot first
        pivot = -1
        for i in range(1, len(nums) - 1):
            if -nums[i-1] < nums[i] < nums[i+1]:
                pivot = i 
                break
        l = -1
        r = -1
        res = []
        if pivot != -1:
            pivot = l , r + 1
            while l >= 0 and r <= len(nums):
                if nums[l] ** 2 >  nums[r] ** 2:
                    res.append(nums[r])
                    l += 1
                else:
                    res.append(nums[l])
                    r -= 1
            while l >= 0:
                res.append(nums[l])
                l += 1
            while r < len(nums):
                res.append(nums[r])
                r -= 1
        else:
            for num in nums:
                res.append(num ** 2)
            
        return res
            

        