class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        pivot_index = 0
        for i in range(1, len(nums)):
            pivot_index += 1
            if nums[i] < nums[i - 1]:
                break
        print('kekeke', pivot_index)
        return min(nums[0], nums[pivot_index])

solution = Solution()
print(solution.findMin( [3,4,5,1,2] ))
