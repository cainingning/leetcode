class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        """
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        """
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [1] * m
        for i in range(m):
            dp[i] = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))