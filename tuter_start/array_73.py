class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for row_z in row:
            for j in range(len(matrix[0])):
                matrix[row_z][j] = 0
        for col_z in col:
            for i in range(len(matrix)):
                matrix[i][col_z] = 0

solution = Solution()
mat = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
print(solution.setZeroes(mat))
print(mat)