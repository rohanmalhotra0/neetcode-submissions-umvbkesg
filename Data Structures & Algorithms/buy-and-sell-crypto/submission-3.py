class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       l = 0
       r = len(prices)-1
       maxProfit = 0
       while l<r: 
            if prices[l] <= prices[r]: 
                profit = prices[r] - prices[l] 
                #print("profit = " , profit , ", L = " , l , " , R = " , r )
                maxProfit = max(maxProfit, profit)
                if 10 - prices[r] > prices[l]- 1:
                    r-=1  
                else:
                    l+=1
            else:
               l+=1

       return maxProfit 
