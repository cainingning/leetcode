class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        single = nums[0]
        for i in range(1, len(nums)):
            single ^= nums[i]

        return single