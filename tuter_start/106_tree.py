# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        root = TreeNode(postorder.pop())
        r_index = inorder.index(root.val)

        root.right = self.buildTree(inorder[r_index + 1:], postorder)
        root.left = self.buildTree(inorder[:r_index], postorder)

        return root


solution = Solution()
root = solution.buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3])

def display(root):
            if root is not None:
                print(root.val)
            else:
                return
            display(root.left)
            display(root.right)

display(root)
def test(tmp):
    if tmp is None:
        print('none', tmp)
    if not tmp:
        print('not', tmp)
test([])
test([1])
test(None)
"""只要是空的list就不是None, """
