class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        """dp, count[i]
                G(n) = F(1, n) + F(2, n) + ... + F(n, n)
                F(i, n) = G(i-1) * G(n-i)	1 <= i <= n 
                f[i]表示i个节点对应的二叉树的数目
                f[i] = sum(f[j-1]* f[i-j]) j=1到i
                """
        f = [0] * (n + 1)
        f[0], f[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                f[i] += f[j - 1] * f[i - j]

        return f[n]

    solution = Solution()
    print(solution.numTrees(3))