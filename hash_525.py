class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        将0换成-1，问题变为求i-j和为0的子序列
        key是和，value是sum对应下标的值
        最后result是返回下标相差的最大值
        """
        if len(nums) == 0:
            return 0
        result = 0
        sum_num = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        hash_map = {}
        hash_map[0] = -1
        for i in range(len(nums)):
            sum_num += nums[i]
            if hash_map.get(sum_num, None) != None:
                result = max(result, i - hash_map[sum_num])
            else:
                hash_map[sum_num] = i

        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxLength([0, 1, 0]))