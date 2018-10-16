class Solution:
    def findPairs_diff(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        sorted_nums = sorted(nums)
        i = 0
        while i < len(sorted_nums):
            for j in range(i + 1, len(sorted_nums)):
                if sorted_nums[j] - sorted_nums[i] == k:
                    result += 1
                    break
            while (i + 1 < len(sorted_nums)) and sorted_nums[i] == sorted_nums[i+1]:
                i += 1
            i += 1


        return result

    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        slide window...注意跳过重复的元素
        """
        sorted_nums = sorted(nums)
        left = 0
        right = 1
        result = 0
        while right < len(sorted_nums):
            if sorted_nums[right] - sorted_nums[left] == k:
                result += 1
                left_num = sorted_nums[left]
                right_num = sorted_nums[right]
                while left < len(sorted_nums) and sorted_nums[left] == left_num:
                    left += 1
                while right < len(sorted_nums) and sorted_nums[right] == right_num:
                    right += 1
            elif sorted_nums[right] - sorted_nums[left] < k:
                right += 1
            else:
                left += 1
            if right == left:
                right += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findPairs([3, 1, 4, 1, 5], k = 2))
