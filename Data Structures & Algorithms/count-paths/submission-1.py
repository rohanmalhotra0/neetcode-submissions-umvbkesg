class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      """
      Can m or n be 0?
      are there any obsticals or just open cells

      """
      dp = [[1] * n for _ in range(m)]
      for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
      return dp[m-1][n-1]
