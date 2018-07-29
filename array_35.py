class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0 or target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        left_index = 0
        right_index = len(nums) - 1
        while left_index < right_index:
            mid = int((left_index - right_index) / 2 + right_index)
            if nums[mid] == target:
                return mid
            elif right_index - left_index == 1:
                return right_index
            elif nums[mid] < target:
                left_index = mid
            else:
                right_index = mid


        return left_index


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert([1,3,5,6], 2))