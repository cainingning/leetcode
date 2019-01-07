class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """O(n^2的时间复杂度)"""
        if len(nums) <= 2 or target is None:
            return 0
        nums.sort()
        nearest_sum = sum(nums[:3])
        for i in range(len(nums) - 2):
            j, k  = i + 1, len(nums) - 1
            while j < k:
                now_sum = nums[i] + nums[j] + nums[k]
                if abs(now_sum - target) < abs(nearest_sum - target):
                    nearest_sum = now_sum
                if now_sum > target:
                    k -= 1
                elif now_sum < target:
                    j += 1
                else:
                    return target

        return nearest_sum

if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumClosest(nums = [-1, 2], target=1))

