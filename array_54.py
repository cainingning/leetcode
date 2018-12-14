class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        if len(matrix[0]) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])
        start_row, end_row, start_col, end_col = 0, m-1, 0, n-1
        result = []
        while start_row <= end_row and start_col <= end_col:
            # from left to right
            for i in range(start_col, end_col+1):
                result.append(matrix[start_row][i])
            # from top to bottom超过一行才能从上到下打印
            if end_row > start_row:
                for j in range(start_row+1, end_row+1):
                    result.append(matrix[j][end_col])
            # from right to left 超过两列两行才能从右到左打印
            if end_row > start_row and end_col > start_col:
                for j in range(end_col - 1, start_col - 1, -1):
                    result.append(matrix[end_row][j])
            # from bottom to top 必须三行两列以上才有这个操作
            if end_row - 1 > start_row and end_col > start_col:
                for i in range(end_row - 1, start_row, -1):
                    result.append(matrix[i][start_col])
            start_row += 1
            end_row -= 1
            start_col += 1
            end_col -= 1

        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.spiralOrder(
        [[3], [2]]
    ))

