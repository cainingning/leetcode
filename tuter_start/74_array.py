class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        i, j, mid = 0, m * n - 1, 0
        while i <= j:
            mid = int((j - i) / 2 + i)
            map_row = mid // n
            map_col = mid - map_row * n
            if matrix[map_row][map_col] == target:
                return True
            elif matrix[map_row][map_col] < target:
                i = mid + 1
            else:
                j = mid - 1

        map_row = mid // n
        map_col = mid - map_row * n
        if matrix[map_row][map_col] == target:
            return True
        else:
            return False

solution = Solution()
print(solution.searchMatrix(matrix = [[1]],
target = 4))