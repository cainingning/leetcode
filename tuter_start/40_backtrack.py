class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.my_dfs(candidates, target, res, [], 0)

        return res

    def my_dfs(self, candidates, remain, res, tmp, index):
        if remain < 0:
            return
        if remain == 0:
            import copy
            res.append(copy.copy(tmp))
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            tmp.append(candidates[i])
            self.my_dfs(candidates, remain - candidates[i], res, tmp, i + 1)
            tmp.remove(candidates[i])

solution = Solution()
print(solution.combinationSum2( candidates = [10,1,2,7,6,1,5], target = 8))