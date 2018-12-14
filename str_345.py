class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        i = 0
        j = len(s) - 1
        s_list = list(s)
        orig = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while i < j:
            if s_list[i] not in orig:
                i += 1
                continue
            if s_list[j] not in orig:
                j -= 1
                continue
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1

        return "".join(s_list)

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseVowels("leetcode"))
