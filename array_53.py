class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        最大子序列和
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_sum = nums[0]
        d = [0] * len(nums)
        d[0] = nums[0]
        for i in range(1, len(nums)):
            d[i] = max(d[i-1] + nums[i], nums[i])
            if d[i] > max_sum:
                max_sum = d[i]

        return max_sum

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-2,-1]))