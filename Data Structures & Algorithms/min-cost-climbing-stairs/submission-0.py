class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)
        def dfs(i, total):
            if i >= len(cost):
                return total if i == len(cost) else 0
            if cache[i] != -1:
                return cache[i]
            
            
            cache[i] = min(dfs(i+1,total + cost[i+2]),dfs(i+2), total + cost[i+2])
            return cache[i]

        return min(dfs(0),dfs(1))