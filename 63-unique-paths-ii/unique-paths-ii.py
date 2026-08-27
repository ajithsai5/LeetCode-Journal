class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0] * n
        dp[0] = 1

        for row in range(m):
            for col in range(n):

                # Obstacle
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0

                # Normal cell
                elif col > 0:
                    dp[col] = dp[col] + dp[col - 1]

        return dp[n - 1]