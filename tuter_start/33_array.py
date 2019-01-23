class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """找到pivot"""
        if len(nums) == 0:
            return -1
        pivot_i = 0
        while pivot_i + 1 < len(nums) and nums[pivot_i] < nums[pivot_i + 1]:
            pivot_i += 1
        pivot_i += 1
        if pivot_i < len(nums) and [pivot_i] == target:
            return pivot_i
        left_i = self.binary_find(0, pivot_i - 1, nums, target)
        if left_i >= 0:
            return left_i
        right_i = self.binary_find(pivot_i, len(nums) - 1, nums, target)
        if right_i >= 0:
            return right_i

        return -1


    def binary_find(self, start, end, nums, target):
        while start < end:
            mid = int((end - start) / 2 + start)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if start == end and start >= 0 and start < len(nums) and nums[start] == target:
            return start
        else:
            return -1


print(Solution().search(nums = [4,5,6,7,0,1,2], target = 3))