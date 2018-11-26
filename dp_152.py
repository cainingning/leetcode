class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
            dp problem
        """
        if len(nums) == 0:
            return 0
        min_d, max_d, result = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            """
            保留最大值和最小值
            """
            tmp1 = nums[i] * min_d
            tmp2 = nums[i] * max_d
            min_d = min(min(tmp1, tmp2), nums[i])
            max_d = max(max(tmp1, tmp2), nums[i])
            result = max(result, max_d)

        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProduct([-2,-3,-1]))