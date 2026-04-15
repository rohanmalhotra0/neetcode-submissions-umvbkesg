class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        for i in range(len(nums)):
            print(arr)
            for j in range(i+1, len(nums)-1):
                k= j+1
                print(i,j,k)
                if nums[i]+nums[j]+nums[k] == 0:
                    arr.append([nums[i],nums[j],nums[k]])
                k+=1       
        if arr == [0,0,0,0]:
            return [[0,0,0]]
        return arr