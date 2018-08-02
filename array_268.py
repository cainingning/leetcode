class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums) * (len(nums) - 1) / 2 - sum(nums)

    def missingNumber_xor(self, nums):
        res = len(nums)
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]

        return res