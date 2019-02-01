class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 0 or k == 0:
            return []
        num = list(range(1, n + 1))
        res = []
        self.my_dfs(num, [], res, k, 0)
        return res


    def my_dfs(self, num, tmp, res, k, index):
        if k == 0:
            import copy
            res.append(copy.copy(tmp))
            return
        for i in range(index, len(num)):
            if num[i] in tmp or len(tmp) > 0 and num[i] < tmp[-1]:
                continue
            tmp.append(num[i])
            self.my_dfs(num, tmp, res, k - 1, index + 1)
            tmp.remove(num[i])


solution = Solution()
print(solution.combine(4, 2))
