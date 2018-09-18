class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        result = []
        for item in nums1:
            index = nums2.index(item)
            if index == -1:
                result.append(index)
            else:
                for i in range(index + 1, len(nums2)):
                    index = i
                    if nums2[i] > item:
                        result.append(nums2[index])
                        break
                if index == -1 or (index == len(nums2) - 1 and nums2[-1] <= item):
                    result.append(-1)

        return result

    def nextGreaterElement_simple(self, nums1, nums2):
        ###数组遍历是从前往后的，引入一个stack记下遍历次序，就可以从后往前遍历。有个反悔的机会
        st = []
        result = []
        store_bigger = {}
        for item in nums2:
            while len(st) > 0 and st[-1] < item:
                store_bigger[st.pop(-1)] = item
            st.append(item)
        for item in nums1:
            result.append(store_bigger.get(item, -1))

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.nextGreaterElement_simple( nums1 = [2,4], nums2 = [1,2,3,4]))
