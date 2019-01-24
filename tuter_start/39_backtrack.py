class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """回溯"""
        if len(candidates) == 0 or target is None:
            return []
        res = []
        candidates.sort()
        self.my_dfs(candidates, target, 0, [], res)

        return res


    def my_dfs(self, candidates, target, index, tmp, res):
        if target < 0:
            return
        if target == 0:
            res.append(tmp)
            return
        for i in range(index, len(candidates)):
            # 从i开始因为可以使用重复元素
            self.my_dfs(candidates, target - candidates[i], i, tmp + [candidates[i]], res)

solution = Solution()
print(solution.combinationSum(candidates = [2,3,5], target = 8))