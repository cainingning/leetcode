class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n_len = len(nums)
        if n_len == 0:
            return [-1, -1]
        start, mid, end = 0, 0, n_len - 1
        while start < end:
            mid = int((end - start) / 2 + start)
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if nums[mid] == target:
            start = mid
        if nums[start] == target:
            start, end = start, start
            while start > 0 and nums[start] == nums[start - 1]:
                start -= 1
            while end + 1 < n_len and nums[end] == nums[end + 1]:
                end += 1
            return [start, end]
        else:
            return [-1, -1]

solution = Solution()
print(solution.searchRange(nums = [1, 1, 3], target = 1))