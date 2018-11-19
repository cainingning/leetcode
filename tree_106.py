# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        """中序和后序得到二叉树"""
        if len(inorder) == 0 or len(postorder) == 0 or len(inorder) != len(postorder):
            return None

        return self.buildTree_core(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)

    def buildTree_core(self, inorder, postorder, i_si, i_ei, p_si, p_ei):
        if p_si > p_ei:
            return None
        root = TreeNode(postorder[p_ei])
        for i in range(i_si, i_ei + 1):
            if inorder[i] == postorder[p_ei]:
                root.left = self.buildTree_core(inorder, postorder, i_si, i - 1, p_si, p_si + i - i_si - 1)
                root.right = self.buildTree_core(inorder, postorder, i + 1, i_ei, p_si + i - i_si, p_ei - 1)
                break

        return root


