class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        """这样速度慢，不好"""

        if len(needle) > len(haystack):
            return -1
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

    def strStr_2(self, haystack, needle):
        """直接用两个指针指有一个bug，比如 mississippi, issip 要从前一个串的每个i处判断，不能直接过去"""
        if len(needle) <= 0:
            return 0
        if len(needle) > len(haystack):
            return -1
        index_1, index_2 = 0, 0
        while index_1 < len(haystack) and index_2 < len(needle):
            if haystack[index_1] == needle[index_2]:
                index_1 += 1
                index_2 += 1
            else:
                index_1 = index_1 - index_2 + 1 # index_1回退到di
                index_2 = 0
            if index_2 == len(needle):
                return index_1 - len(needle)

        return -1

    def get_next(self, needle):
        next = [0] * len(needle)
        next[0] = -1
        j, k = 0, -1
        while j < len(needle) - 1:
            if k == -1 or needle[j] == needle[k]:
                if needle[j] == needle[k]:
                    next[j] = next[k]
                else:
                    next[j] = k
                j += 1
                k += 1
            else:
                k = next[k]
        return next

    def strStr_kmp(self, haystack, needle):

        """"""
        """KMP算法是解决字符串中pattern定位问题"""
        if len(needle) == 0:
            return 0
        i, j = 0, 0
        next = self.get_next(needle)
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(needle):
                return i - j

        return -1


solution = Solution()
print(solution.strStr_kmp("abaaaabc", "bc"))
