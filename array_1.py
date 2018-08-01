class Solution:
    def twoSum_better(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        key是这个数需要几才能变成target，值是这个数的索引
        """
        if len(nums) <= 1:
            return []
        hash_dict = {}
        for i in range(len(nums)):
            if nums[i] in hash_dict:
                return [hash_dict[nums[i]], i]
            else:
                hash_dict[target - nums[i]] = i
        return []


    def twoSum_test(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0 or nums[0] * 2 > target or nums[-1] * 2 < target:
            return []
        first_num = 0
        last_num = len(nums) - 1
        result = []
        new_nums = sorted(nums)
        while first_num < last_num:
            if new_nums[first_num] + new_nums[last_num] == target:
                first_index = nums.index(new_nums[first_num])
                last_index = nums.index(new_nums[last_num])
                result.extend([first_index, last_index])
                return result
            elif new_nums[first_num] + new_nums[last_num] < target:
                first_num += 1
            else:
                last_num -= 1

        return result

    def twoSum_NN(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

