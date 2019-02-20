# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        """先序遍历，然后左节点置空，右节点指向下一个节点,
        这里的点在于保存前一个便利的节点。"""
        if root is None:
            return
        last = TreeNode(-1)
        stack = [root]
        while len(stack) > 0:
            node = stack.pop(-1)
            last.left = None
            last.right = node
            last = node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
