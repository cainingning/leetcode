class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            tmp = [1] * (i + 1)
            for j in range(1, len(tmp) - 1):
                tmp[j] = res[-1][j - 1] + res[-1][j]
            res.append(tmp)

        return res

solution = Solution()
print(solution.generate(5))