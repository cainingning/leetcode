class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        """这个是超时的"""
        res = []
        l = [i for i in range(1, n + 1)]
        self.dfs_core(res, [], l)

        if len(res) < k :
            return ""
        res = [str(i) for i in res[k - 1]]
        return "".join(res)

    def dfs_core(self, res, tmp, num):
        if len(tmp) == len(num):
            import copy
            res.append(copy.copy(tmp))
            return

        for i in range(len(num)):
            if num[i] in tmp:
                continue
            tmp.append(num[i])
            self.dfs_core(res, tmp, num)
            tmp.remove(num[i])

    def getPermutation_2(self, n, k):
        """"""
        """一个数学问题。比如4
        [1, 2, 3, 4]
        1 + 3！--6中组合
        2 + 3！--6
        3 + 3！--6
        4 + 3！--6
        如果要找k=15那么必定第一位置是3，接下来在[1, 2, 4]中寻找第3个,
        第二位2, 在[1, 4]找第1个，14.3214结束"""
        num = list(range(1, n + 1))
        k -= 1 # num已经是第一个变换了。
        res = ''
        while n > 0:
            n -= 1
            import math
            index, k = divmod(k, math.factorial(n))
            res += str(num[index])
            num.remove(num[index])

        return res

solution = Solution()
print(solution.getPermutation_2(4, 16))