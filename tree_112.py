# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if root is None:
            return False

        return self.recv_hasPathSum(root, sum)

    def recv_hasPathSum(self, node, sum):
        if node is None:
            return  False

        if node.left is None and node.right is None and sum == node.val:
            return True

        return self.recv_hasPathSum(node.left, sum - node.val) | self.recv_hasPathSum(node.right, sum - node.val)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(-2)
    # root.left = TreeNode(4)
    root.right = TreeNode(-3)
    # root.left.right = TreeNode(11)
    # root.right.left = TreeNode(13)
    # root.right.right = TreeNode(4)

    print(solution.hasPathSum(root, -5))
