# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif root.left is None or root.right is None:
            return self.minDepth(root.left) + self.minDepth(root.right) + 1
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

solution = Solution()
head = TreeNode(1)
head.left = TreeNode(2)
print(solution.minDepth(head))