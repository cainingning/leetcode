class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pre_list = [1]
        if rowIndex < 0 or rowIndex > 33:
            return []
        for i in range(1, rowIndex + 1):
            now_list = [1] * (i + 1)
            for j in range(1, len(now_list) -1):
                now_list[j] = pre_list[j - 1] + pre_list[j]
            pre_list = now_list

        return pre_list

if __name__ == '__main__':
    solution = Solution()
    print(solution.getRow(3))
