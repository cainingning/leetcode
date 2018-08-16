class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        """
        从n^2开始，每次顺时针旋转当前矩阵，并且在此基础上添加一行
        ||  =>  |9|  =>  |8|      |6 7|      |4 5|      |1 2 3|
                         |9|  =>  |9 8|  =>  |9 6|  =>  |8 9 4|
                                             |8 7|      |7 6 5|
        """
        result = []
        min_num = n * n + 1
        while min_num > 1:
            min_num, max_num = min_num - len(result), min_num
            result = [list(range(min_num, max_num))] + [*zip(*result[::-1])]

        return result

    def generateMatrix_walk(self, n):
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n * n):
            print("i, j, di, dj", i, j, di, dj)
            A[i][j] = k + 1
            if A[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A

if __name__ == '__main__':
    solution = Solution()
    print(solution.generateMatrix_walk(3))