class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = ""
        str = str.strip()
        if len(str) <= 0:
            return 0
        if str[0] == '-':
            flag = -1
            start = 1
        elif str[0] == '+':
            flag = 1
            start = 1
        elif str[0].isnumeric():
            flag = 1
            start = 0
        else:
            return 0
        for i in range(start, len(str)):
            if not str[i].isnumeric():
                break
            result += str[i]
        if len(result) == 0:
            return 0
        result = flag * int(result)
        if result < -1 * 2**31:
            return -1 * 2**31
        elif result > 2**31 -1:
            return 2** 31 -1
        else:
            return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.myAtoi("+1"))

