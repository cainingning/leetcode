class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        index1 = 0
        index2 = 0
        result = []
        while index1 < len(nums1) and index2 < len(nums2):
            while index1 < len(nums1) and index2 < len(nums2) and nums1[index1] < nums2[index2]:
                index1 += 1
            while index1 < len(nums1) and index2 < len(nums2) and nums1[index1] > nums2[index2]:
                index2 += 1
            if  index1 < len(nums1) and index2 < len(nums2) and nums1[index1] == nums2[index2]:
                result.append(nums1[index1])
                index1 += 1
                index2 += 1

        return result
        ###array349的解答，去重
        ### return list(set(result))

if __name__ == '__main__':
    solution = Solution()
    print(solution.intersect([7,2,2,4,7,0,3,4,5], [3,9,8,6,1,9,3]))