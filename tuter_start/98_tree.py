# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes = [(root, None, None)]
        while len(nodes) > 0:
            node, low_b, up_b = nodes.pop(0)
            if node.left:
                if node.left.val < node.val:
                    if low_b and node.left.val <= low_b:
                        return False
                    nodes.append((node.left, low_b, node.val))
                else:
                    return False
            if node.right:
                if node.right.val > node.val:
                    if up_b and up_b <= node.right.val:
                        return False
                    nodes.append((node.right, node.val, up_b))
                else:
                    return False
        return True

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print(Solution().isValidBST(root))

