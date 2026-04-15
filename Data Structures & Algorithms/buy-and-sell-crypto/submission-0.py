class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1 = float("inf")
        max1 = prices[0]
        for i in range(len(prices)):
            if prices[i] > max1:
                max1 = prices[i]
            if prices[i] < min1:
                min1 = prices[i]
        output = max1 - min1 
        
        if max1 == min1:
            return 0
        
        return output - 1
            
            