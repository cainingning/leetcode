# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if abs(self.get_height(root.left) - self.get_height(root.right)) <= 1:
            return self.isBalanced(root.left) & self.isBalanced(root.right)
        else:
            return False

    def get_height(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        else:
            return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def isBalanced_2(self, root):

        return self.check(root) != -1

    def check(self, root):
        if root is None:
            return 0
        left = self.check(root.left)
        right = self.check(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

solution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
print(solution.isBalanced(root))
