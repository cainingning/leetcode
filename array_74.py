class Solution:
    def searchMatrix_stupid(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = 0
        if m > 0:
            n = len(matrix[0])
        if m == 0 or n == 0 or target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        h_index = 0
        lo_index = h_index + 1
        while lo_index < m:
            if matrix[lo_index][-1] == target:
                return True
            elif matrix[h_index][-1] < target and matrix[lo_index][-1] > target:
                break
            else:
                h_index += 1
                lo_index += 1
        if matrix[0][-1] >= target:
            lo_index = 0
        print(lo_index)
        ### tmp_m is target row
        l_index = 0
        r_index = n
        while l_index < r_index:
            mid = (l_index + r_index) // 2
            if matrix[lo_index][mid] == target:
                return True
            elif matrix[lo_index][mid] > target:
                r_index = mid - 1
            else:
                l_index = mid + 1

        if l_index >= 0 and l_index < n and matrix[lo_index][l_index] == target:
            return True

        return False

    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        l_index = 0
        r_index = m * n - 1
        while l_index < r_index:
            mid = (l_index + r_index) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] < target:
                l_index = mid + 1
            else:
                r_index = mid - 1
        if matrix[l_index // n][l_index % n] == target:
            return True

        return False


if __name__ == '__main__':
    solution = Solution()
    matrix = [[1]]
    print(solution.searchMatrix(matrix, 1))