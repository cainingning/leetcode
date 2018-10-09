class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        """
        3+3+3+3加到多少能加到14，次数6就是24/3的结果。优化算法第一次加3，第二次2个3，第三次4个三
        """
        if dividend == 0:
            return 0
        a = abs(dividend)
        b = abs(divisor)
        result = 0
        while b <= a:
            temp_sum = b
            count = 1
            while temp_sum * 2 <= a:
                count += count
                temp_sum += temp_sum
            a = a - temp_sum
            result += count
        if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
            result *= -1

        if result > pow(2, 31) - 1 or result < pow(2, 31) * -1:
            return pow(2, 31) - 1

        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.divide(7, -3))

