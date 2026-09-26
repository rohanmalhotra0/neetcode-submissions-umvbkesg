class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        self.dfs(0,[],nums)
        return self.res
    def dfs(self,i,cur,nums):
        if i >= len(nums):
            self.res.append(cur.copy())
            return
       
        cur.append(nums[i+1])
        self.dfs(i+1, cur, nums)

        cur.pop()
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        self.dfs(i+1, cur, nums)


