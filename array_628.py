class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        三个最大正数想成或者两个最小负数乘以最大正数
        """
        if len(nums) <= 2:
            return 0
        sorted_nums = sorted(nums)
        max1 = sorted_nums[-1] * sorted_nums[-2] * sorted_nums[-3]
        max2 = sorted_nums[0] * sorted_nums[1] * sorted_nums[-1]
        return max(max1, max2)



