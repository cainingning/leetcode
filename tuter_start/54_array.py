class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        res = []
        start_c, end_c = 0, len(matrix[0]) - 1
        start_r, end_r = 0, len(matrix) - 1
        while start_c <= end_c and start_r <= end_r:
            for i in range(start_c, end_c + 1):
                res.append(matrix[start_r][i])
            #从上到下打印，只有至少两行才行
            if end_r - start_r >= 1:
                for j in range(start_r + 1, end_r + 1):
                    res.append(matrix[j][end_c])
            #从右到左打印，至少有两行两列
            if end_r - start_r >= 1 and end_c - start_c >= 1 :
                for i in range(end_c - 1, start_c - 1, -1):
                    res.append(matrix[end_r][i])
            #从下到上打印，至少三行两列
            if end_r - start_r >= 2 and end_c - start_c >= 1:
                for j in range(end_r - 1, start_r, -1):
                    res.append(matrix[j][start_c])
            start_r += 1
            end_r -= 1
            start_c += 1
            end_c -= 1

        return res


solution = Solution()
print(solution.spiralOrder( [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

