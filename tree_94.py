# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        左-根-右
        """
        if root is None:
            return []
        result = []
        self.inorderTraversal_core(root, result)

        return result

        
    def inorderTraversal_core(self, node, result):
        if node is None:
            return
        self.inorderTraversal_core(node.left, result)
        result.append(node.val)
        self.inorderTraversal_core(node.right, result)