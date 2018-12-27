class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        暴力法
        time:O(N^2)
        space:O(1)
        """
        if len(nums) == 0 or target is None:
            return []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    def twoSum_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        哈希表 key是该值，value是该值对应的索引
        time:O(N)
        space:O(N)
        """
        if len(nums) == 0 or target is None:
            return []
        store = {}
        for i in range(len(nums)):
            if store.get(nums[i], None) is None:
                store[nums[i]] = i
            need_num = target - nums[i]
            if store.get(need_num, None) != None and store[need_num] != i:
                return sorted([i, store[need_num]])

        return []

if __name__ == '__main__':
    solution  = Solution()
    print(solution.twoSum_2([3, 2, 4], target=6))
