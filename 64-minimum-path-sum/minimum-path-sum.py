class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [0] * n

        # First row
        dp[0] = grid[0][0]

        for col in range(1, n):
            dp[col] = dp[col - 1] + grid[0][col]

        # Remaining rows
        for row in range(1, m):
            # First column
            dp[0] = dp[0] + grid[row][0]

            for col in range(1, n):
                dp[col] = grid[row][col] + min(dp[col], dp[col - 1])

        return dp[n - 1]