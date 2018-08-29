class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """返回数组的全排列
        将整组数中的所有的数分别与第一个数交换，这样就总是在处理后n-1个数的全排列
        """
        if len(nums) == 0:
            return []

        result = []
        self.combine(nums, result, 0)
        # print(result)
        # result = [list(x.split()) for x in result]

        return result
    def combine(self, nums,  result, index):
        """
        :param result:结果列表
        :param index: 当前处理字符的索引
        :param tmp: 已处理的暂存字符串
        :return:
        """
        if index == len(nums):
            import copy
            # print(nums)
            result.append(copy.deepcopy(nums))
            return
        else:
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                self.combine(nums, result, index + 1)
                nums[i], nums[index] = nums[index], nums[i]

if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))