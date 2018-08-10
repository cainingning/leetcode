class Solution:
    def findDuplicates_extraSpace(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) <= 0:
            return []
        result = []
        dict = {}
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        for k, v in dict.items():
            if v >= 2:
                result.append(v)

        return result

    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        找到nums中出现两次的数字，其余数字只出现一次.
        数字是1---n
        """
        if nums is None or len(nums) <= 0:
            return []
        result = []
        for i in nums:
            nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
            if nums[abs(nums[i]) - 1] < 0:
                result.append(nums[i])

        return result






