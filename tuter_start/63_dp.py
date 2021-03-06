class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(1, n):
            if obstacleGrid[0][i] == 0 and dp[0][i - 1] > 0:
                dp[0][i] = 1
        for j in range(1, m):
            if obstacleGrid[j][0] == 0 and dp[j - 1][0] > 0:
                dp[j][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


solution = Solution()
print(solution.uniquePathsWithObstacles([
  [0,0],
  [1,1],
  [0,0]
]))