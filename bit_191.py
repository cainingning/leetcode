class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        """输入是无符号正数"""
        if n == 0:
            return 0
        count = 0
        while n > 0 :
            count += n & 1
            n = n >> 1

        return count

if __name__ == '__main__':
    solution = Solution()
    x = 12
    print(solution.hammingWeight(x))