class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """O(n)"""
        # if len(nums) == 0:
        #     return -1
        # pivot_num = nums[0]
        # for i in range(1, len(nums)):
        #     if nums[i] < pivot_num:
        #         pivot_num = nums[i]
        # return pivot_num
        """O(logn)"""
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = int((end + start) / 2)
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        return min(nums[0], nums[start])

if __name__ == '__main__':
    solution = Solution()
    print(solution.findMin( [4,5,6,7,0,1,2]))

