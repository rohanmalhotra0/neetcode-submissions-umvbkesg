class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        memo = [float('inf')] * len(costs)
        colors = [0,1,2]
        def dfs(i, num):
            if i >= len(costs):
                return 0 
            if memo[i] != -1: 
                return memo[i]
            # memo[i] should return min cost of taking red-blue-green
            for color in colors:
                if num != color:
                    memo[i] = min(memo[i], dfs(i+1, color) + costs[i][num])
           
            return memo[i]
        return dfs(0,-1)