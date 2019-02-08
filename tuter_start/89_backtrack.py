class Solution:
    def grayCode(self, n):
        res = self.grayCode_core(n)
        print(res)
        for i in range(len(res)):
            res[i] = int(res[i], 2)

        return res
    def grayCode_core(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        """格雷码的构造规则，n+1位的格雷码= 0+n位格雷码+ 1+n位逆序的格雷码"""
        res = []
        if n == 0:
            res = ['0']
        elif n == 1:
            res = ['0', '1']
        else:
            pre = self.grayCode_core(n - 1)
            res = ['0' + x for x in pre] + ['1' + x for x in pre[::-1]]

        return res

solution = Solution()
print(solution.grayCode(3))