class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        """O(n)的时间复杂度
        但是需要额外的存储空间
        不好！"""
        x = str(x)
        i, j = 0, len(x) - 1
        while i < j:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        return True

    def isPalindrome_2(self, x):
        """

        :param x:
        :return:
        """
        """log10(n)的时间复杂度
        将数字进行反转，如果是回文肯定和原先数字一样，如果不一样不是回文，但是有溢出的风险。
        所以可以只反转后裔一半数字"""
        """如果最后一位是0那么它是回文它必须是0"""
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        former_num = x
        latter_num = 0
        while former_num > latter_num:
            last_num = former_num % 10
            former_num = former_num // 10
            latter_num = latter_num * 10 + last_num
        """如果有偶数位，前一半等于后一半，如果是基数位，那么是一样的"""
        if former_num == latter_num or former_num == latter_num // 10:
            return True
        else:
            return False

    def isPalindrome_3(self, x):
        """beat 99.64%的人"""
        str_x = str(x)
        if x < 0:
            return False
        if x == 0:
            return True
        elif str_x[-1] == '0':
            return False
        str_y = str_x[::-1]
        if str_x == str_y:
            return True
        else:
            return False


