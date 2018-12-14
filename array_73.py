class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m <= 0:
            return
        n = len(matrix[0])
        if n <= 0:
            return
        row_set = set()
        col_set = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        for i in row_set:
            for j in range(n):
                matrix[i][j] = 0
        for j in col_set:
            for i in range(m):
                matrix[i][j] = 0



if __name__ == '__main__':
    solution = Solution()
    m = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
    print(solution.setZeroes(m))

    print(m)
