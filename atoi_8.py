class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str.strip()) <= 0:
            return 0
        valid_end = 0
        strip_str = str.strip()
        if len(strip_str) <= 0 or strip_str[0] not in ["+", "-"] and not strip_str[0].isdigit() or strip_str[0] == "0":
            return 0
        strip_str = strip_str.lstrip("0")

        symbol = 1
        if strip_str[0] == "-":
            symbol = -1
        if strip_str[0] in ["+", "-"]:
            strip_str = strip_str[1:].lstrip("0")
        if len(strip_str) <= 0:
            return 0

        for i in range(len(strip_str)):
            if strip_str[i].isdigit():
                valid_end += 1
            else:
                break
        sub_str = strip_str[:valid_end]
        if len(sub_str) <= 0:
            return 0

        MAX_INT = "2147483647"
        MIN_INT = "-2147483648"
        if symbol == -1 and self.str_cmp(sub_str, MIN_INT[1:]) in [0, 1]:
            return int(MIN_INT)
        if symbol == 1 and self.str_cmp(sub_str, MAX_INT) in [0, 1]:
            return int(MAX_INT)

        return symbol * int(sub_str)

    def str_cmp(self, str1, str2):
        if str1 == str2:
            return 0
        sub_str1 = str1
        if str1[0] in ["+", "-"]:
            sub_str1 = str1[0:]
        sub_str2 = str2
        if str2[0] in ["+", "-"]:
            sub_str2 = str2[0:]
        if len(sub_str1) > len(sub_str2):
            return 1
        elif len(sub_str1) < len(sub_str2):
            return -1
        for i in range(len(sub_str1)):
            if sub_str1[i] < sub_str2[i]:
                return -1
            elif sub_str1[i] > sub_str2[i]:
                return 1

        return 1

if __name__ == '__main__':
    solution = Solution()
    # print(solution.myAtoi("42"))
    print(solution.myAtoi("0-1"))
    # print(solution.myAtoi( "4193 with words"))
    # print(solution.myAtoi( "words and 987"))
    # print(solution.myAtoi("-91283472332"))


