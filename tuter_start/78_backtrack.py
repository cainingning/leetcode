class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """返回一个集合所有的子集合"""
        if len(nums) == 0:
            return []
        res = []
        nums.sort()
        self.my_dfs(nums, 0, [], res)

        return res


    def my_dfs(self, nums, index, tmp, res):
        import copy
        res.append(copy.copy(tmp))
        for i in range(index, len(nums)):
            tmp.append(nums[i])
            self.my_dfs(nums, i + 1, tmp, res)
            tmp.remove(nums[i])

        return

solution = Solution()
print(solution.subsets([1, 2, 3]))

