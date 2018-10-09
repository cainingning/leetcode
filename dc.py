class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ### 从左到右升序，从上到下升序
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        tmp_m = 0
        tmp_n = n - 1
        while tmp_m < m and tmp_n >= 0:
            if matrix[tmp_m][tmp_n] == target:
                return True
            elif matrix[tmp_m][tmp_n] < target:
                ###去掉一行
                tmp_m += 1
            else:
                tmp_n -= 1
        if tmp_m < m and tmp_n >= 0 and matrix[tmp_m][tmp_n] == target:
            return True

        return False

