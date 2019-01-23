class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or target is None:
            return -1
        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((right - left) / 2 + left)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

print(Solution().searchInsert([1,3,5,6], 5))
