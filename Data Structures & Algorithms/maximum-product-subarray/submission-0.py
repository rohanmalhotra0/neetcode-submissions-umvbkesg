class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cache = [-1] * nums
        maxProd = 0 
        def backtrack(i, total):
            if i >= len(nums):
                maxProd = max(total, maxProd)
                return 0 
            
            for num in range(i, nums):
                if cache[num] != -1:
                    return cache[num]
                cache[num] = total * cache[num]
                backtrack(i+1, cache[num])
                total = total / cache[num]
                
        backtrack(0,1)
        return maxProd