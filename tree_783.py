# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = [root]
        import sys
        min_num = sys.maxsize
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left:
                min_num = min(min_num, current.val - current.left.val)
                queue.append(current.left)
            if current.right:
                min_num = min(min_num, current.right.val - current.val)
                queue.append(current.right)


        return min_num