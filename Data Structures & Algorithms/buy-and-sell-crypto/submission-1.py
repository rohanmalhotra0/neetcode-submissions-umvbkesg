class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       l = 0
       r = len(prices)-1
       maxProfit = 0
       while l<r:
            if prices[l] < prices[r]:
               profit = prices[r]- prices[l] 
               maxProfit = max(maxProfit, profit)
               r-=1
            else:
                l+=1
       return maxProfit 
