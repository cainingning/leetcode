class Solution:
    def numDecodings_2(self, s):
        if len(s) == 0:
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if i != 1 and s[i - 2: i] < '27' and s[i - 2: i] > '09':
                dp[i] += dp[i - 2]
        return dp[-1]


solution = Solution()
print(solution.numDecodings_2('227'))
