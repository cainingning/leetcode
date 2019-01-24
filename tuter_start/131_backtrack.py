class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        """将s切割使得每个子串都是回文子串"""
        res = []
        self.my_dfs(s, [], res, 0)

        return res

    def my_dfs(self, s, tmp, res, start_index):
        if start_index == len(s):
            import copy
            res.append(copy.copy(tmp))
            return
        for i in range(start_index, len(s)):
            if self.is_para(s, start_index, i):
                tmp.append(s[start_index: i + 1])
                self.my_dfs(s, tmp, res, i + 1)
                tmp.pop(-1)

    def is_para(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True

solution = Solution()
print(solution.partition('aab'))