class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        """顺时针旋转二维数组"""
        """顺序读每一行，填充到每一列从后往前"""
        if len(matrix) == 0 or len(matrix) != len(matrix[0]):
            print(len(matrix), len(matrix[0]))
            return
        m = len(matrix)
        n = len(matrix[0])
        res = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][n - i - 1] = matrix[i][j]
        for i in range(m):
            for j in range(n):
                matrix[i][j] = res[i][j]

        return

    def rotate_clockwise(self, matrix):
        """"""
        """
        /*
         * clockwise rotate 先x对称再对角线对称
         如果是逆时针旋转，先y对称再对角线对称
        * first reverse up to down, then swap the symmetry 
        * 1 2 3     7 8 9     7 4 1
        * 4 5 6  => 4 5 6  => 8 5 2
        * 7 8 9     1 2 3     9 6 3  
        """
        if len(matrix) == 0 or len(matrix) != len(matrix[0]):
            return
        i, j = 0, len(matrix) - 1
        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return

solution = Solution()
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(len(matrix), len(matrix[0]))
solution.rotate_clockwise(matrix)
print(matrix)
