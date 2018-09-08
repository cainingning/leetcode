class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        """
        if m <= 0 or n <= 0:
            return 0
        dp = [1] * m
        for i in range(m):
            dp[i] = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]


        return dp[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePaths(7, 3))