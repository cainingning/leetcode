class Solution:
    # time complexity too high O(n^2)
    def maxArea_test(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height is None or len(height) <= 1:
            return 0
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                max_area = max(max_area, abs(j - i) * min(height[i], height[j]))


        return max_area

    # O(n) trick
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height is None or len(height) <= 1:
            return 0
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            max_area = max(max_area, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area




if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))