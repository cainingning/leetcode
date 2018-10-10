# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        return self.isSymmetric_core(root.left, root.right)

    def isSymmetric_core(self, l_c, r_c):
        if l_c is None and r_c is None:
            return True
        if l_c is None or r_c is None:
            return False
        if l_c.val != r_c.val:
            return False
        if l_c.val == r_c.val:
            return self.isSymmetric_core(l_c.left, r_c.right) & self.isSymmetric_core(l_c.right, r_c.left)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)

    solution = Solution()
    print(solution.isSymmetric(root))