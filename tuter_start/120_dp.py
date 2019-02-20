class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return -1
        dp = []
        for item in triangle:
            dp.append([0] * len(item))
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j - 1 < 0:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j]
                elif j > len(triangle[i - 1]) - 1:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j])

        return min(dp[-1])

solution = Solution()
print(solution.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))