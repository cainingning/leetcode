class Solution(object):
    def cmp(self, num_a, num_b):
        num_a = str(num_a)
        num_b = str(num_b)
        str1 = num_a + num_b
        str2 = num_b + num_a

        if int(str1) > int(str2):
            return 1
        elif int(str1) < int(str2):
            return -1
        else:
            return 0


    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        """定义一种排序规则，对数组进行排序，mn>nm就把m排在n前面"""
        if nums is None or len(nums) <= 0:
            return ""
        import functools
        nums = sorted(nums, key=functools.cmp_to_key(self.cmp), reverse=True)
        nums = [str(_i) for _i in nums]

        result = "".join(nums)

        if result[0] == '0':
            return '0'

        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.largestNumber([10, 2]))




