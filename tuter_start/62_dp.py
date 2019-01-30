class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """dp[i][j]表示从原点到ij点时有多少条路径，而这个与它上面点的路径数和左边点的路径数有关，是和"""
        if m == 0:
            return 0
        dp = [[1 for i in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


solution = Solution()
print(solution.uniquePaths(7, 3))