class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """O(N^3)的时间复杂度
        需要注意的点是去重"""
        if len(nums) <= 3:
            return []
        res = []
        nums.sort()
        for i in range(0, len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target_3 = target - nums[i]
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                target_2 = target_3 - nums[j]
                k, l = j + 1, len(nums) - 1
                while k < l:
                    if nums[k] + nums[l] == target_2:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1
                        k += 1
                        l -= 1
                    elif nums[k] + nums[l] < target_2:
                        k += 1
                    else:
                        l -= 1

        return res


    def test_perfect(self, nums, target):
        result = []
        N = len(nums)
        if N < 4:
            return result
        nums = sorted(nums)
        for i in range(N - 3):
            # if sum(nums[i:i + 4]) > target or sum(nums[-4:]) < target:
            #     break
            # if nums[i] + sum(nums[-3:]) < target:
            #     continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target3 = target - nums[i]
            for j in range(i + 1, N - 2):
                # if sum(nums[j:j + 3]) > target3 or sum(nums[-3:]) < target3:
                #     break
                # if nums[j] + sum(nums[-2:]) < target3:
                #     continue
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                target2 = target3 - nums[j]
                left = j + 1
                right = N - 1
                while (left < right):
                    if nums[left] + nums[right] == target2:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]: left += 1;
                        while left < right and nums[right] == nums[right - 1]: right -= 1;
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] < target2:
                        left += 1
                    else:
                        right -= 1
        return result

solution = Solution()
print(solution.fourSum([-3,-2,-1,0,0,1,2,3], 0))
print(solution.test_perfect([-3,-2,-1,0,0,1,2,3], 0))
