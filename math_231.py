class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bit_rep = bin(n)
        count = 0
        for i in bit_rep[2: ]:
            if i == '1':
                count += 1
        if count == 1:
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfTwo(-16))