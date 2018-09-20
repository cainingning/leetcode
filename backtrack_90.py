class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0 or nums is None:
            return []
        result = []
        self.subsetsWithDup_core(sorted(nums), result, [], 0)

        return result

    def subsetsWithDup_core(self, nums, result, tmp, index):
        if tmp not in result:
            import copy
            result.append(copy.copy(tmp))
        for i in range(index, len(nums)):
            tmp.append(nums[i])
            self.subsetsWithDup_core(nums, result, tmp, i + 1)
            tmp.pop(-1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsetsWithDup([4,4,4,1,4]))
