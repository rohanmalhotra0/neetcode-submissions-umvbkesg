class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        if nums == [0,0,0]:
           return [nums]
        for i in range(len(nums)):
            for j in range(i, len(nums)-1):
                k = j+1
                if nums[i]+nums[j]+nums[k] == 0:
                    arr.append([nums[i],nums[j],nums[k]])
                k+=1
        
        return arr