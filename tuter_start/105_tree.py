# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0 or len(inorder) == 0 or len(preorder) != len(inorder):
            return None
        root = TreeNode(preorder[0])
        r_index = inorder.index(preorder[0])
        if r_index == len(inorder) - 1:
            root.left = self.buildTree(preorder[1:], inorder[:-1])
        elif r_index - 1 < 0:
            root.right = self.buildTree(preorder[1:], inorder[1:])
        else:
            left_num = r_index - 1 + 1
            root.left = self.buildTree(preorder[1: 1 + left_num], inorder[:r_index])
            root.right = self.buildTree(preorder[left_num + 1:], inorder[r_index + 1:])

        return root

solution = Solution()
root = solution.buildTree([3,9,20,15,7], [9,3,15,20,7])
def display(root):
    if root is not None:
        print(root.val)
    else:
        return
    display(root.left)
    display(root.right)
display(root)