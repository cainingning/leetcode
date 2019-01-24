class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """列举所有的排列形式"""
        res = []
        nums.sort()
        self.my_dfs(nums, [], res)

        return res


    def my_dfs(self, nums, tmp, res):
        if len(tmp) == len(nums):
            import copy
            res.append(copy.copy(tmp))

            return
        for i in range(0, len(nums)):
            if nums[i] in tmp:
                continue
            tmp.append(nums[i])
            self.my_dfs(nums, tmp, res)
            tmp.remove(nums[i])


solution = Solution()
print(solution.permute([1, 2, 3]))
