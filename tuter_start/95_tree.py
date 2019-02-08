class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return [[]]
        return self.my_dfs(1, n + 1)

    def my_dfs(self, start, end):
        if start == end:
            return None
        res = []
        for i in range(start, end):
            for left in self.my_dfs(start, i) or [None]:
                for right in self.my_dfs(i + 1, end) or [None]:
                    node = TreeNode(i)
                    node.left = left
                    node.right = right
                    res.append(node)
        return res
