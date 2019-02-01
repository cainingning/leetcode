class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return 
        i, j, k = 0, 0, 0
        for item in nums:
            if item == 0:
                i += 1
            elif item == 1:
                j += 1
            else:
                k += 1
        for x in range(0, i):
            nums[x] = 0
        for y in range(i, i + j):
            nums[y] = 1
        for z in range(i + j, i + j + k):
            nums[z] = 2


solution = Solution()
num = [2,0,2,1,1,0]
print(solution.sortColors(num))
print(num)

