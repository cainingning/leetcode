class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        二分查找
        """
        if len(nums) == 0 or target not in nums:
            return [-1, -1]
        i = 0
        j = len(nums) - 1
        mid = 0
        while i <= j:
            mid = int((i + j) / 2)
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        start_index = mid
        end_index = mid
        while start_index >= 0:
            if nums[start_index] == target:
                start_index -= 1
            else:
                break
        while end_index < len(nums):
            if nums[end_index] == target:
                end_index += 1
            else:
                break

        return [start_index + 1, end_index - 1]




if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange([1, 4], 4))