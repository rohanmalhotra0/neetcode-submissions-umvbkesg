class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxPrice = 0
        for price in prices:
            minPrice = min(price, minPrice)
            maxProfit = max(maxProfit,price - minPrice)        
        return maxPrice






