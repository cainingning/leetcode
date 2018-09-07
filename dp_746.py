class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 0:
            return 0
        length = len(cost)
        dp = [0] * length
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, length):
            dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])

        return min(dp[-2], dp[-1])

if __name__ == '__main__':
    solution = Solution()
    print(solution.minCostClimbingStairs([10, 15, 20]))