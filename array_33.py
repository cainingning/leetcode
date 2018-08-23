class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 0 or (len(nums) == 1 and target != nums[0]):
            return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = int(l + (r - l) / 2)
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[mid] == target:
                return mid
            if nums[mid] > nums[l]:
                if nums[mid] > target and nums[l] < target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and nums[r] > target:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.search(nums = [4,5,6,7,0,1,2], target = 3))