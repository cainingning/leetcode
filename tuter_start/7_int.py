class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        string是一种不可变的数据类型
        O(n)的时间复杂度，还有各种类型转换
        """
        x_s = list(str(x))
        if len(x_s) <= 1:
            return x
        sign = 1
        if x_s[0] == '-':
            sign = -1
            x_s = x_s[1:]

        i, j = 0, len(x_s)-1
        while i < j:
            x_s[i], x_s[j] = x_s[j], x_s[i]
            i += 1
            j -= 1
        # print(x_s)
        result = sign * int("".join(x_s))
        if result < -1 * pow(2, 31) or result > pow(2, 31) - 1:
            return 0
        else:
            return result

    def reverse_2(self, x):
        """
        rev是返回结果，依次将x弹出最末尾的意味， 将其添加到rev的第一位。注意判断溢出
        log(n)的时间复杂度
        :return:
        """
        """这里不要调用pow()计算非常的缓慢！"""
        flag = 1
        if x < 0 :
            flag = -1
        x = flag * x
        result = 0
        while x != 0:
            pop_n = x % 10
            x = x // 10
            """判断新的result溢出与否"""
            if result > ((2 ** 31 - 1) / 10) or (result == (2 ** 31 - 1) / 10 and pop_n > 7):
                return 0
            result = result * 10 + pop_n

        return flag * result

if __name__ == '__main__':
    solution = Solution()
    # print(solution.reverse_2(0))
    # print(solution.reverse_2(123))
    print(solution.reverse_2(-123))
    # print(pow(2, 31) - 1, pow(2, 31))
