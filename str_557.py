class Solution(object):
    def reverse_str(self, s):
        i = 0
        str_list = list(s)
        j = len(str_list) - 1
        print(str_list)

        while i < j:
            tmp = str_list[j]
            str_list[j] = str_list[i]
            str_list[i] = tmp
            i += 1
            j -= 1

        return "".join(str_list)

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list = s.strip().split(" ")
        if len(str_list) == 0:
            return ""
        for i in range(len(str_list)):
            str_list[i] = self.reverse_str(str_list[i])


        return " ".join(str_list)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords("Let's take LeetCode contest"))