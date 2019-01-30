class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """dp 超时"""
        if len(nums) == 0:
            return True
        n = len(nums)
        index_store = [False] * n
        index_store[-1] = True
        for i in range(n - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j < n and index_store[i + j] == True:
                    index_store[i] = True
                    break

        return index_store[0]
    def canJump_2(self, nums):
        n = len(nums) - 1
        i = 0
        reach = 0
        while i < n and i <= reach:
            reach = max(nums[i] + i, reach)
            i += 1
        return reach >= n



solution = Solution()
print(solution.canJump_2([2, 0]))
