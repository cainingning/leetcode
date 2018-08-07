class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        valid = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[valid]:
                valid += 1
                nums[valid] = nums[i]
        return valid + 1

if __name__ == '__main__':
    solution = Solution()
    l1 = [0,0,1,1,1,2,2,3,3,4]
    l2 = []
    print(solution.removeDuplicates(l2))
    print(l1)