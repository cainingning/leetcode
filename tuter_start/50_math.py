class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / x * self.myPow(1 / x, -(n + 1))
        if n == 0:
            return 1
        if n == 2:
            return x * x
        if n % 2 == 0:
            return self.myPow(self.myPow(x, n // 2), 2)
        else:
            return x * self.myPow(self.myPow(x, n // 2), 2)

solution = Solution()
print(solution.myPow(2.0, 10))