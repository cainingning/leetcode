# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        result = []
        self.preOrder_core(root, result)

        return result

    def preOrder_core(self, node, result):
        if node is None:
            return
        result.append(node.val)
        if node.left:
            self.preOrder_core(node.left, result)
        if node.right:
            self.preOrder_core(node.right, result)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(3)
    root.left.left = TreeNode(2)
    # root.right.right = TreeNode(7)
    # root.right.right.left = TreeNode(7)

    # print(solution.getDepth(root))
    print(solution.preorderTraversal(root))
