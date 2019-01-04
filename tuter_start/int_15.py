class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # if len(nums) <= 2:
        #     return []
        nums = sorted(nums)
        # if nums[0] > 0 or nums[-1] < 0:
        #     return []
        result = []
        for k in range(len(nums)-2):
            if k == 0 or nums[k] > nums[k - 1]:
                i = k + 1
                j = len(nums) - 1
                while i < j:
                    now_sum = nums[k] + nums[i] + nums[j]
                    if now_sum < 0:
                        i += 1
                    elif now_sum > 0:
                        j -= 1
                    else:
                        result.append([nums[k], nums[i], nums[j]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i - 1]:
                            i += 1
                        while i < j and nums[j] == nums[j + 1]:
                            j -= 1

        return result


so = Solution()
print(so.threeSum([0, 0, 0]))