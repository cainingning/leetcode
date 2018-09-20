class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0 or nums is None:
            return []
        result = []
        self.subsets_core(nums, result, [], 0)

        return result

    def subsets_core(self, nums, result, tmp, index):
        """

        :param nums:
        :param result:
        :param tmp: 临时存储此次的
        :param index:现在处理的是index元素
        :return:
        """
        import copy
        result.append(copy.copy(tmp))
        for i in range(index, len(nums)):
            tmp.append(nums[i])
            self.subsets_core(nums, result, tmp, i + 1)
            tmp.pop(-1)

if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1,2,3]))