# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        """深度优先遍历树"""
        """父节点入栈，父节点出栈，右节点入栈，左节点入栈"""
        if root is None:
            return None
        tmp = [root]
        while len(tmp) > 0:
            pop_node = tmp.pop(-1)
            if pop_node.right:
                tmp.append(pop_node.right)
            if pop_node.left:
                tmp.append(pop_node.left)
            if len(tmp) > 0 :
                pop_node.right = tmp[-1]
                pop_node.left = None

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    solution.flatten(root)
    while root:
        print(root.val)
        root = root.right