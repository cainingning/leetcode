class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        位运算，每位的和都是3N或者3N+1, 其中那个1是那个只出现一次的数字贡献的
        """
        if len(nums) == 0:
            return -1
        result = 0
        for i in range(32):
            mask = 1 << i
            print(mask)
            count = 0
            for j in range(len(nums)):
                if mask & nums[j] > 0:
                    count += 1
            print('count', count)
            if count % 3 :
                result |= mask

        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]))
