class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]
        def backtrack(amount, i):
            if amount == 0:
                return 1 
            if i >= len(coins):
                return  0
            if memo[i][a] != -1:
                return memo[i][a]

            if amount >= coins[i]:
                res = backtrack(amount - coins[i], i)
                res += backtrack(amount, i+1)
            memo[i][a] = res
            return res
        return backtrack(amount, 0)
        
