class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        """返回这个子串所有对应的可能的ip地址"""
        if len(s) == 0:
            return []
        res = []
        # self.my_dfs(res, "", )

    def my_dfs(self, res, tmp, s, index):
        return