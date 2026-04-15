class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        for i in range(len(nums)):
            j= i + 1
            k =j + 1
            while k < len(nums):
                if nums[i]+nums[j]+nums[k] == 0 and [nums[i],nums[j],nums[k]] not in arr:
                        arr.append([nums[i],nums[j],nums[k]]) 
                j+=1 
                k+=1 
   
        return arr
       