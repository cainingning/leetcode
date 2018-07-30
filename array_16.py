class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        O(N^2)
        将数组排序，对数组的每一个元素设置首尾两个指针，时刻保持此时最接近target的sum
        """
        if nums is None or len(nums) <= 2:
            return 0
        sum = nums[0] + nums[1] + nums[2]
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            left_index = i + 1
            right_index = len(nums) - 1
            while left_index < right_index:
                now_sum = nums[i] + nums[left_index] + nums[right_index]
                if abs(sum - target) > abs(now_sum - target):
                     sum = now_sum
                     if sum == target:
                         return sum
                if now_sum < target:
                    left_index += 1
                else:
                    right_index -= 1

        return sum

if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumClosest([1,2,4,8,16,32,64,128], 82))