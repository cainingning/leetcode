class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """找到乘积最大的连续子串，保留最正的数字和最负的数字,因为如果下一个数字是正的，那此时的最大数是这个数
        乘以之前的最大数，而若下一个数字是负的，那此时最大数是这个数乘以之前的最负数"""
        if len(nums) == 0:
            return None
        dp_max = nums[0]
        dp_min = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            xx = nums[i] * dp_max
            yy = nums[i] * dp_min
            dp_max = max(nums[i], xx, yy)
            dp_min = min(nums[i], xx, yy)
            res = max(res, dp_max)
        return res

solution = Solution()
print(solution.maxProduct([-2, -3, -4]))