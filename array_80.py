class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return 0
        if len(nums) <= 2:
            return len(nums)
        store_dict = {}
        for item in nums:
            if store_dict.get(item, 0) == 0:
                store_dict[item] = 1
            else:
                store_dict[item] += 1
        index = 0
        result_index = 0
        while index < len(nums):
            count = min(2, store_dict[nums[index]])
            for i in range(result_index, result_index + count):
                nums[i] = nums[index]
            index += store_dict[nums[index]]
            result_index += count

        return result_index


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates(nums = [1,2,2]))

