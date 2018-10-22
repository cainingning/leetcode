class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        logN的时间复杂度
        题目给定的是第一个元素和最后一个元素是无限小的，所以一定有一个波峰，然后只需要只要一个元素它的右邻居比它小就行了。
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        if nums[left] > nums[right]:
            return left
        else:
            return right

if __name__ == '__main__':
    solution = Solution()
    print(solution.findPeakElement([1,2]))