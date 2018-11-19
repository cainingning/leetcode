# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0 or len(inorder) == 0 or len(preorder) != len(inorder):
            return None

        return self.buildTree_core(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)

    def buildTree_core(self, preorder, inorder, p_si, p_ei, i_si, i_ei):
        if p_si > p_ei:
            return None
        root = TreeNode(preorder[p_si])
        for i in range(i_si, i_ei + 1):
            if inorder[i] == preorder[p_si]:
                root.left = self.buildTree_core(preorder, inorder, p_si + 1, p_si + i - i_si, i_si, i - 1)
                root.right = self.buildTree_core(preorder, inorder, p_si + i - i_si + 1, p_ei, i + 1, i_ei)
                break

        return root


