class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        memo = {}

        def dfs(i, prevColor):
            if i >= len(costs):
                return 0

            if (i, prevColor) in memo:
                return memo[(i, prevColor)]

            minCost = float('inf')

            for color in range(3):
                if color != prevColor:
                    cost = costs[i][color] + dfs(i + 1, color)
                    minCost = min(minCost, cost)

            memo[(i, prevColor)] = minCost
            return minCost

        return dfs(0, -1)