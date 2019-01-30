class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """有正数有负数，动态规划"""
        if len(nums) == 0:
            return -1
        dp = [0] * len(nums) # 以i为结尾的子串的最大值
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i - 1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]

        return max(dp)


    def maxSubArray_2(self, nums):
        """"""
        """O(n**2),超时"""
        if len(nums) == 0:
            return -1
        max_num = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if max_num < sum(nums[i: j + 1]):
                    max_num = sum(nums[i: j + 1])

        return max_num

# solution = Solution()
# print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4],))
s = 'a'
print(s.split()[-1])