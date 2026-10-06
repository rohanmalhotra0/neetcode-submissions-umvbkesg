class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(perm):
            if len(perm) == len(nums):
                res.add(tuple(perm))
                return

            for i in range(len(nums)):
                if nums[i] != float("-inf"): # Check for no resue we want unique 
                    
                    perm.append(nums[i])     # this is your take step 
                    nums[i] = float("-inf")
                    backtrack(perm)

                    nums[i] = perm[-1]
                    perm.pop()         # 17 18 are your reset / Skip step  

        backtrack([])
        return list(res)
