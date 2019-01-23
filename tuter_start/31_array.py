class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """从右往左第一个逆序的a[i]，找a[i-1...len()]里从右往左第一个比a[i]大的数字将两者交换，然后重排序后面的数字"""
        index = len(nums) - 2
        if index <= -1:
            return
        while index >= 0 and nums[index] >= nums[index + 1]:
            index -= 1
        if index >= 0:
            replace_index = len(nums) - 1 # index+1到最后的里面比nums[index]大的最小的\\
            while replace_index >= 0 and nums[replace_index] <= nums[index]:
                replace_index -= 1
            nums[index], nums[replace_index] = nums[replace_index], nums[index]
        self.my_reverse(index + 1, len(nums) - 1, nums)

        return
    def my_reverse(self, start, end, nums):
        if start >= end or start < 0 or end >= len(nums):
            return
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return


solution = Solution()
nums = [5, 1, 1]
solution.nextPermutation(nums)
print(nums)