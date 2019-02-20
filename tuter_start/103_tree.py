# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """广度优先遍历，然后把偶数位置的都反转"""
        if root is None:
            return []
        res = []
        tmp = []
        nodes = [(root, 1)]
        while len(nodes) > 0:
            node, layer = nodes.pop(0)
            tmp.append((node, layer))
            if node.left:
                nodes.append((node.left, layer + 1))
            if node.right:
                nodes.append((node.right, layer + 1))
            if layer != len(res):
                res.append([node.val])
            else:
                res[-1].append(node.val)
        for i in range(len(res)):
            if i % 2 != 0:
                res[i] = res[i][::-1]
        return res

solution = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(solution.zigzagLevelOrder(root))




