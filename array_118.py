class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        results = [[1]]
        for i in range(2, numRows + 1):
            temp = [0] * i
            temp[0] = 1
            temp[-1] = 1
            for j in range(1, i - 1):
                if j - 1 >= 0:
                    temp[j] = results[-1][j - 1] + results[-1][j]
                else:
                    temp[j] = results[-1][j]
            results.append(temp)

        return results

if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(0))