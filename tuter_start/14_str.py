class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        """64mms，击败22.64%"""
        if len(strs) <= 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        min_str = strs[0]
        for s in strs:
            if len(s) < len(min_str):
                min_str = s
        index = 0
        flag = True
        while index < len(min_str):
            for s in strs:
                if len(s) == 0 or (index < len(s) and s[index] != min_str[index]):
                    flag = False
                    break
            if flag:
                index += 1
            else:
                break

        return min_str[:index]

    def longestCommonPrefix_2(self, strs):
        """"""
        """44s,击败99.57的解法"""
        if len(strs) == 0:
            return
        min_str = strs[0]
        for s in strs:
            if len(s) < len(min_str):
                min_str = s
        for s in strs:
            while not s.startswith(min_str):
                min_str = min_str[:-1]
                if len(min_str) == 0 :
                    return ''
        return min_str

so = Solution()
print(so.longestCommonPrefix_2(["a", "aa"]))
