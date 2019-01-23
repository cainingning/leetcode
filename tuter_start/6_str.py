class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        """
        z字形变换
        """
        if len(s) <= 1 or numRows <= 1:
            return s
        result = [[0] for _ in range(min(numRows, len(s)))]
        start_row = 0
        s_index = 0
        go_down = False
        while s_index < len(s):
            result[start_row].append(s[s_index])
            s_index += 1
            if start_row == 0 or start_row == numRows - 1:
                go_down = not go_down
            if go_down:
                start_row += 1
            else:
                start_row -= 1

        final_result = ""
        for i in result:
            # print("".join(i[1:]))
            final_result += "".join(i[1:])

        return final_result

    def convert_2(self, s, numRows):
        """
        """
        """第一行和最后一行奇书列的时候是没有元素添加的"""
        if len(s) <= 1 or numRows <= 1:
            return s
        result = [''] * min(numRows, len(s))
        curr_row = 0
        go_down = 1
        for i in range(len(s)):
            result[curr_row] += s[i]
            if curr_row == 0:
                go_down = 1
            elif curr_row == numRows - 1:
                go_down = -1
            curr_row += go_down

        return "".join(result)


if __name__ == '__main__':
    solution = Solution()
    print(solution.convert_2("aaaa", 3))