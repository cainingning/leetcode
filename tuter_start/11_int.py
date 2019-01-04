class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """暴力法O(N**2)会超时
        不好！"""
        max_water = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                water = (j - i) * min(height[i], height[j])
                if water > max_water:
                    max_water = water

        return max_water

    def maxArea_2(self, height):
        """"""
        """双指针。因为蓄水池的宽度越宽则面积越可能大O(N)
        击败28%的人。不好
        """
        i, j = 0, len(height) - 1
        max_water = 0
        while i < j:
            max_water = max(max_water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_water


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea_2( [1,8,6,2,5,4,8,3,7]))