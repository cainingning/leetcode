class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0 or nums is None:
            return 0
        dict = {}
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        for k, v in dict.items():
            if v >= len(nums) / 2:
                return k

if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([3,2,3]))
