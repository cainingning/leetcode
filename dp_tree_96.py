class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        """考虑i节点，1-i-1必须是左子树，i+1到n必须是右子树"""
        if n <= 0:
            return 0
        if n <= 1:
            return 1
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]

        return dp[n]

if __name__ == '__main__':
    solution = Solution()
    print(solution.numTrees(3))
