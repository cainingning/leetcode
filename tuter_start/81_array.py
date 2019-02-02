class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0 or target is None:
            return False
        pivot_i = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                pivot_i = i
                break
        return self.binary_search(nums, 0, pivot_i - 1, target) \
               or self.binary_search(nums, pivot_i, len(nums) - 1, target)

    def binary_search(self, nums, left, right, target):
        if left > right:
            return False
        mid = 0
        while left <= right:
            mid = int((right - left) / 2 + left)
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # if nums[mid] == target:
        #     return True
        # else:
        return False

solution = Solution()
print(solution.search(nums = [2,5,6,0,0,1,2], target = 0))