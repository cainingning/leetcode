class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result_list = [float('-inf'), float('-inf'), float('-inf')]
        for i in nums:
            if i not in result_list:
                if i > result_list[0]:
                    result_list = [i, result_list[0], result_list[1]]
                elif i > result_list[1]:
                    result_list = [result_list[0], i, result_list[1]]
                elif i > result_list[2]:
                    result_list[2] = i
        if float('-inf') in result_list:
            return max(nums)
        else:
            return result_list[2]

if __name__ == '__main__':
    solution = Solution()
    print(solution.thirdMax([1, 2, 2, 5, 3, 5]))

