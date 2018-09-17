# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        import sys
        return self.isValidBST_core(root, sys.maxsize, -1 * sys.maxsize - 1)

    def isValidBST_core(self, node, max_num, min_num):
        if node is None:
            return True
        if node.val >= max_num or node.val <= min_num:
            return False

        return self.isValidBST_core(node.left, node.val, min_num) and self.isValidBST_core(node.right, max_num,  node.val)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(20)
    print(solution.isValidBST(root))