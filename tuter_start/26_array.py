class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        valid_n = 1
        j = 1
        while j < len(nums):
            if nums[j] > nums[valid_n - 1]:
                nums[valid_n] = nums[j]
                valid_n += 1
            j += 1

        return valid_n

solution = Solution()
print(solution.removeDuplicates( [0,0,1,1,1,2,2,3,3,4]))