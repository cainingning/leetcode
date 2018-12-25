class Solution(object):
    def maxWidthRamp_stupid(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 0:
            return 0
        max_p = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if j > i and A[j] >= A[i] and j - i > max_p:
                    max_p = j - i

        return max_p

    def maxWidthRamp_slide(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        """滑窗模块，从n开始尝试，直到窗口长度= 0"""
        if len(A) <= 0:
            return 0
        window_size = len(A) - 1
        while window_size > 0:
            left = 0
            right = window_size
            while right < len(A):
                if A[right] >= A[left]:
                    return right - left
                else:
                    left += 1
                    right += 1
            window_size -= 1

        return 0

    """
    我们把索引号,和数值组成元组,按数值进行排序.

    接下来遍历这个元组序列,找出索引号差值最大的
    """

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxWidthRamp_slide([6,0,8,2,1,5]))
