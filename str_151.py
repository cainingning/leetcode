class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.strip().split()
        i = 0
        j = len(s_list) - 1
        while i < j:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1

        return " ".join(s_list)

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords("the sky is blue"))

