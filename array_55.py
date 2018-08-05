class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # far代表现在能jump到的最远距离
        far = 0
        for i in range(len(nums)):
            if far < i :
                return False
            far = max(i + nums[i], far)

        return True