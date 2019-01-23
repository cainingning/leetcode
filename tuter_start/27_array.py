class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        """O(n)时间 O(1)空间， """
        i, j = 0, 0
        while j < len(nums):
            if nums[j] == val:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1

        return i

    def removeElement_2(self, nums, val):
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1

        return j + 1

solution = Solution()
print(solution.removeElement_2( nums = [3,2,2,3], val = 3))
