class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        """首先做右对角变换，其次旋转180度"""
         



if __name__ == '__main__':
    solution = Solution()
    x = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    solution.rotate(matrix=x)
    print(x)
