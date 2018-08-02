class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left_index = 0
        center_index = 0
        right_index = len(nums) - 1
        while center_index < right_index:
            if nums[center_index] == 0:
                nums[left_index], nums[center_index] = nums[center_index], nums[left_index]
                left_index += 1
                center_index += 1
            elif nums[center_index] == 1:
                center_index += 1
            else:
                nums[center_index], nums[right_index] = nums[right_index], nums[center_index]
                right_index -= 1


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 0, 2]
    solution.sortColors(nums)
    print(nums)