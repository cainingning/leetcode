class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        if len(needle) > len(haystack):
            return -1
        temp1 = 0
        temp2 = 0
        find_index = 0
        while temp1 < len(haystack) and temp2 < len(needle):
            while temp1 < len(haystack) and temp2 < len(needle) and haystack[temp1] == needle[temp2]:
                temp1 += 1
                temp2 += 1
            if temp2 == len(needle):
                return find_index
            while temp1 < len(haystack) and temp2 < len(needle) and haystack[temp1] != needle[temp2]:
                temp1 = find_index + 1
                temp2 = 0
                find_index += 1
                if len(haystack) - temp1 < len(needle) - temp2:
                    return -1

        if find_index >= len(needle):
            return -1

        return find_index

    def strStr_simple(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr_simple("bbaa", "aab"))
