class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        将nums[nums[i] - 1]数字如果是正变成负数证明出现过，如果是负不变，最后把正数加到结果中
        """
        result = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0 :
                nums[abs(nums[i]) - 1] = nums[abs(nums[i]) - 1] * (-1)
        # print(nums)
        for i in range(len(nums)):
            if nums[i] > 0 :
                result.append(i + 1)

        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))