class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        """
        位运算 a[i] ^ b[i] 是无进位相加， a[i] & b[i]是进位
        carry得到每一位的进位
        a ^ b 得到无进位相加结果
        """
        carry = 0
        while b > 0:
            carry = a & b
            print('carry', carry)
            a = a ^ b
            b = carry << 1

        return a

if __name__ == '__main__':
    solution = Solution()
    print(solution.getSum(123, 45))