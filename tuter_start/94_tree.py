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
        if root is None:
            return []
        res = []
        self.core(root, res)

        return res

    def core(self, node, res):
        if node is None:
            return
        self.core(node.left, res)
        res.append(node.val)
        self.core(node.right, res)

    def inorder_norev(self, root):
        if root is None:
            return []
        res = []
        cur = root
        sta = []
        while cur or len(sta) > 0:
            if cur:
                sta.append(cur)
                cur = cur.left
            else:
                cur = sta.pop(-1)
                res.append(cur.val)
                cur = cur.right

        return res

solution = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(solution.inorderTraversal(root))
print(solution.inorder_norev(root))


