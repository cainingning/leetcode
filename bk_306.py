class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        """
        首先找到第一个数，范围是0-len-1/2.因为至少有3个数。设定为i
        其次找第二个数，范围是i-j。
        第三个数的长度至少大于一二个数里最长的。
        """
        for i in range(int((len(num) - 1) / 2) + 1):
            if num[0].startswith('0') and i + 1 >= 2:
                break
            j = i + 1
            while j < len(num):
                ### 第三个数的长度要比前前两个数字大
                if len(num) - j < i or len(num) - j < j - i + 1:
                    break
                if num[i+1] == '0' and (j - i) >= 2:
                    break
                num1 = num[:i+1]
                num2 = num[i+1:j+1]
                if self.backTrack(num[j+1:], num1, num2):
                    return True
                j += 1

        return False

    def backTrack(self, remain, num1, num2):
        if remain == "":
            return True
        num3 = str(int(num1) + int(num2))
        if not remain.startswith(num3):
            return False

        return self.backTrack(remain[len(num3):], num2, num3)

if __name__ == '__main__':
    solution = Solution()
    print(solution.isAdditiveNumber("199001200"))



