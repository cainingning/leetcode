class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """写的不好"""
        if len(nums) <= 2:
            return len(nums)
        store = {}
        for item in nums:
            if store.get(item) and store[item] <= 1:
                store[item] += 1
            elif store.get(item) is None:
                store[item] = 1
        count = 0
        for k, v in store.items():
            for i in range(v):
                nums[count] = k
                count += 1

        return count
    def removeDuplicates_2(self, nums):
        """"""
        """允许最多重复两次，用双指针，一个指实际的，一个值原先的"""
        if len(nums) <= 2:
            return len(nums)
        cnt = 1
        res_p, cur_p = 1, 1
        while cur_p < len(nums):
            if nums[cur_p] != nums[cur_p - 1]:
                cnt = 1
                nums[res_p] = nums[cur_p]
                res_p += 1
            elif cnt < 2:
                cnt += 1
                nums[res_p] = nums[cur_p]
                res_p += 1
            cur_p += 1
        return res_p



solution = Solution()
nums = [1,1,1,2,2,3]
print(solution.removeDuplicates_2(nums))
print(nums)
