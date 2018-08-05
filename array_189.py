class Solution:
    def rotate_timeout(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k % len(nums)):
            temp = nums[-1]
            for j in range(len(nums) - 2, -1, -1):
                nums[j + 1] = nums[j]
            nums[0] = temp

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = k % len(nums)
        temp = nums[-l:]
        nums[l:] = nums[0:-l]
        nums[0:l] = temp

    def rotate_discuss(self, nums, k):
        k = k % len(nums)
        n = len(nums)
        nums[:] = nums[n - k:] + nums[:n - k]


if __name__ == '__main__':
    solution = Solution()
    l1 =   [1,2,3,4,5,6,7]
    solution.rotate(l1, 3)
    print(l1)