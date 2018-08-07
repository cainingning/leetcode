class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) <= 0:
            return []
        sorted_nums = sorted(nums)
        if sorted_nums[0] > 0 or sorted_nums[-1] < 0:
            return []
        result = []
        for l_index in range(len(sorted_nums)):
            if l_index > 0 and sorted_nums[l_index] == sorted_nums[l_index - 1]:
                continue
            m_index = l_index + 1
            r_index = len(sorted_nums) - 1
            while m_index < r_index:
                sum = sorted_nums[l_index] + sorted_nums[m_index] + sorted_nums[r_index]
                if sum < 0:
                    m_index += 1
                elif sum > 0:
                    r_index -= 1
                else:
                    result.append([sorted_nums[l_index], sorted_nums[m_index], sorted_nums[r_index]])
                    m_index += 1
                    while m_index < r_index and sorted_nums[m_index] == sorted_nums[m_index - 1]:
                        m_index += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))