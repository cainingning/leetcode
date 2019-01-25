class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        """返回两个字符串的乘积"""
        if len(num1) >= 110 or len(num2) >= 110:
            return ''
        l1 = list(num1)
        l2 = list(num2)
        if len(l1) < len(l2):
            l1, l2 = l2, l1
        res = []
        for i in range(len(l2)):
            res.append(int(l2[i]) * int("".join(l1)) * (10 ** (len(l2) - i - 1)))

        res = sum(res)

        return str(res)


solution = Solution()
print(solution.multiply("123456789", "987654321"))