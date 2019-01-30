class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """斐波那契数列，f(n) = f(n-1) + f(n-2)"""
        if n <= 2:
            return n
        a, b = 1, 1
        c = a + b
        for i in range(3, n):
            a = b
            b = c
            c = a + b

        return c + b
solution = Solution()
print(solution.climbStairs(2))
