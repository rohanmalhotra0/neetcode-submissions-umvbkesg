class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        def dfs(i, nums, cur):
            if sum(cur) == target:
                res.append(cur.copy())
                return
            if sum(cur) > target:
                return 

            for num in nums:
                cur.append(num)
                dfs(i+1 ,nums, cur)
                cur.pop
        dfs(0, nums, [])
        return res