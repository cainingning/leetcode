class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []
        result = [[0] * n for _ in range(n)]
        start_row, end_row, start_col, end_col = 0, n-1, 0, n-1
        number = 1
        while start_row <= end_row and start_col <= end_col:
            for i in range(start_col, end_col+1):
                result[start_row][i] = number
                number += 1
            if end_row > start_row:
                for i in range(start_row + 1, end_row + 1):
                    result[i][end_col] = number
                    number += 1
            if end_row > start_row and end_col > start_col:
                for i in range(end_col-1, start_col-1, -1):
                    result[end_row][i] = number
                    number += 1
            if end_row - 1 > start_row and end_col > start_col:
                for i in range(end_row-1, start_row, -1):
                    result[i][start_col] = number
                    number += 1
            start_row +=1
            end_row -= 1
            start_col += 1
            end_col -= 1

        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.generateMatrix(1))
