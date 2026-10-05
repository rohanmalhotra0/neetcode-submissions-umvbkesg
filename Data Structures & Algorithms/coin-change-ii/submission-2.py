class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        def backtrack(amount, i):
            if amount == 0:
                return 1 
            if i >= len(coins):
                return  0
            res = 0
            if amount >= coins[i]:
                res = backtrack(amount - coins[i], i)
                res += backtrack(amount, i+1)
            return res
        return backtrack(amount, 0)
        
