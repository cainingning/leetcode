# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        result = []
        queue = [root]
        temp = [root.val]
        while len(queue) > 0:
            if self.sum_num(temp) == sum:
                result.append(temp)

            remove_node = queue.pop(0)
            if remove_node.left:
                queue.append(remove_node.left)

            if remove_node.right:
                queue.append(remove_node.right)

    def sum_num(self, list):
        return sum(list)
if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(-2)
    # root.left = TreeNode(4)
    root.right = TreeNode(-3)
    # root.left.right = TreeNode(11)
    # root.right.left = TreeNode(13)
    # root.right.right = TreeNode(4)

    print(solution.hasPathSum(root, -5))
