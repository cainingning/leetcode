class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        self.my_dfs(nums, [False] * len(nums), [], res)

        return res


    def my_dfs(self, nums, used, tmp, res):
        if len(tmp) == len(nums):
            import copy
            res.append(copy.copy(tmp))
            return

        for i in range(len(nums)):
            if used[i] or (i > 0 and (not used[i - 1]) and nums[i] == nums[i - 1]):
                continue
            tmp.append(nums[i])
            used[i] = True
            self.my_dfs(nums, used, tmp, res)
            tmp.pop(-1)
            used[i] = False

solution = Solution()
print(solution.permuteUnique([2,2,1,1]))
