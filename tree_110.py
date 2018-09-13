# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if abs(self.getDepth(node.left) - self.getDepth(node.right)) > 1:
                return False

        return True

    def getDepth(self, root):
        if root is None:
            return 0
        return max(self.getDepth(root.left) + 1, self.getDepth(root.right) + 1)

    def isBalanced_clever(self, root):

        return self.getHeight(root) != -1

    def getHeight(self, root):
        if root is None:
            return 0
        left_height = self.getHeight(root.left)
        if left_height == -1:
            return -1
        right_height = self.getHeight(root.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height + 1, right_height + 1)

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    # root.right.right.left = TreeNode(7)

    # print(solution.getDepth(root))
    print(solution.isBalanced_clever(root))