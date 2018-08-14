class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None or len(nums) <= 0 or k <= 0:
            return 0
        return self.quickSortCore(nums, 0, len(nums) - 1, len(nums) - k)

    def quickSortCore(self, nums, l_index, r_index, k):
        if l_index > r_index:
            return 0
        i = l_index
        j = r_index
        pivot = nums[l_index]
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= pivot:
                i += 1
            nums[j] = nums[i]
        nums[i] = pivot
         # print("pivot", nums[i], i)
        if k == i:
            # print("k----", i, "nums[4]", nums[i])
            return nums[i]
        elif k < i:
            return self.quickSortCore(nums, l_index, i - 1, k)
        else:
            return self.quickSortCore(nums, i + 1, r_index, k)

if __name__ == '__main__':
    solution =Solution()
    x = solution.findKthLargest([3,2,1,5,6,4], 2)
    print(x)