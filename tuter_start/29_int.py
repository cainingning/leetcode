class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        """不用除法乘法，取模做除法
        用二分法"""
        if divisor == 0 or (dividend == -(2 ** 31) and divisor == -1):
            return 2 ** 31 - 1
        """除法只有可能是下溢出"""

        if dividend <= 0 and divisor < 0 or (dividend >= 0 and divisor > 0):
            sign = 1
        else:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            tmp = divisor
            times = 1
            while dividend >= tmp << 1:
                tmp = tmp << 1
                times = times << 1
            dividend -= tmp # dividend = divisor * times + 余数(玉树一定比被除数小，所以这个while有等号)
            result += times

        return result if sign == 1 else -1 * result

print(Solution().divide(10, -2))
