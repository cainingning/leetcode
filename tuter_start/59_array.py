class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []
        num = 1
        res = [[0] * n for i in range(n)]
        start_r, end_r, start_c, end_c = 0, n - 1, 0, n - 1
        # from left to right
        while start_r <= end_r and start_c <= end_c:
            for i in range(start_c, end_c + 1):
                res[start_r][i] = num
                num += 1
            # from top to bottom
            if end_r > start_r:
                for i in range(start_r + 1, end_r + 1):
                    res[i][end_c] = num
                    num += 1
            if end_c > start_c and end_r > start_r:
                for i in range(end_c - 1, start_c - 1, -1):
                    res[end_r][i] = num
                    num += 1
            if end_r > start_r + 1 and end_c > start_c:
                for i in range(end_r - 1, start_r , -1):
                    res[i][start_r] = num
                    num += 1
            start_r += 1
            end_r -= 1
            start_c += 1
            end_c -= 1

        return res
solution = Solution()
print(solution.generateMatrix(1))