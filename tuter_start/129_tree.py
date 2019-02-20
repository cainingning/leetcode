# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """不要把数字转换成字符串，直接int操作时间节省很多。"""
        if root is None:
            return 0
        res = 0
        tmp = [(root, root.val)]
        while len(tmp) > 0:
            node, val = tmp.pop(0)
            if node.left:
                tmp.append((node.left, val * 10 + node.left.val))
            if node.right:
                tmp.append((node.right, val * 10 + node.right.val))
            if node.left is None and node.right is None:
                res += val

        return res
