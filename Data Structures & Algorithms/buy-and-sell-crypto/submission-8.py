class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , 1
        maxProfit = 0
        while r < len(prices):
            buy = prices[l]
            sell = prices[r]
            if buy > sell:
                l = r 
                
            else:
                maxProfit = max(maxProfit,  sell - buy)
            r += 1
        return maxProfit



        