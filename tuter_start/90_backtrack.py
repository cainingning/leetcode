class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """返回一个集合的所有子集合，有重复元素"""
        res = []
        nums.sort()
        self.my_dfs(nums, 0, [], res)

        return res

    def my_dfs(self, nums, index, tmp, res):
        import copy
        res.append(copy.copy(tmp))
        i = index
        while i < len(nums):
            if i > index and nums[i] == nums[i - 1]:
                i += 1
                continue
            tmp.append(nums[i])
            self.my_dfs(nums, i + 1, tmp, res)
            tmp.remove(nums[i])
            i += 1

        return

solution = Solution()
print(solution.subsetsWithDup([1, 2, 2, 3]))
