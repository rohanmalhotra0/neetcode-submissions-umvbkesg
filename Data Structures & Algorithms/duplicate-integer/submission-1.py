class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # make a map : goal dont store dupes and compare lengths
         map1 = {}
         # for loop add all ints in list to map
         for i in range (len(nums)):
            map1[nums[i]] = i
         print(map1.keys())
         # check if map length is the same as list length
         # return true if it does false if not
         return len(map1.keys()) != len(nums) 
         