class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        res = [1]
        for i in range(1, rowIndex + 1):
            tmp = [1] * (i + 1)
            for j in range(1, len(tmp) - 1):
                tmp[j] = res[j - 1] + res[j]
            res = tmp

        return res

solution = Solution()
print(solution.getRow(3))
