class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if nums1 is None or nums2 is None or len(nums2) != n or len(nums1) != m + n:
            return
        res_p = m + n - 1
        p_1 = m - 1
        p_2 = n - 1
        while p_1 >= 0 and p_2 >= 0:
            if nums1[p_1] > nums2[p_2]:
                nums1[res_p] = nums1[p_1]
                p_1 -= 1
            else:
                nums1[res_p] = nums2[p_2]
                p_2 -= 1
            res_p -= 1
        while p_1 >= 0:
            nums1[res_p] = nums1[p_1]
            res_p -= 1
            p_1 -= 1
        while p_2 >= 0:
            nums1[res_p] = nums2[p_2]
            res_p -= 1
            p_2 -= 1

solution = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(solution.merge(nums1, m, nums2, n))
print(nums1)
