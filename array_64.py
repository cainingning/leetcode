class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        动态规划
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        d = grid
        m = len(d)
        n = len(d[0])
        for i in range(1, m):
            d[i][0] = d[i - 1][0] + d[i][0]
        for j in range(1, n):
            d[0][j] = d[0][j - 1] + d[0][j]
        for i in range(1, m):
            for j in range(1, n):
                d[i][j] += min(d[i - 1][j], d[i][j - 1])

        return d[-1][-1]
