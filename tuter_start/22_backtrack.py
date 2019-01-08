class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.core(res, '(', n - 1, n)

        return res

    def core(self, res, temp, left_n, right_n):
        if left_n == 0 and right_n == 0:
            import copy
            res.append(copy.copy(temp))
            return
        if left_n > 0:
            self.core(res, temp + '(', left_n - 1, right_n)

        if right_n > left_n:
            self.core(res, temp + ')', left_n, right_n - 1)


solution = Solution()
print(solution.generateParenthesis(3))