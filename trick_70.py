class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        f1 = 1
        f2 = 1
        f3 = f1 + f2
        for i in range(2, n):
            f1 = f2
            f2 = f3
            f3 = f1 + f2

        return f3

if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(2))