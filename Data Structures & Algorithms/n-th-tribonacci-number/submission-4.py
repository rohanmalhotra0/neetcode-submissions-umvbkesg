class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [-1] * (n + 1)
        def backtrack(n):
            if n == 1 or n == 2:
                return 1
            if n == 0:
                return 0
            if memo[n] != -1 : return memo[n]
            memo[n] = backtrack(n - 1) + backtrack(n - 2) + backtrack(n - 3)
            return memo[n]
        return backtrack(n)
        